import pandas as pd
import numpy as np
import os
import math
import random
import traceback
import matplotlib.pyplot as plt

import configuration
import tools
import choose_tel

df_re = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv',
                    encoding='utf-8')
df_co = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_node&tel.csv', encoding='utf-8')
df_tel = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_tel_station.csv',
                     encoding='utf-8')


# 读取迪杰斯特路径文件
f = open("迪杰斯特拉路径.txt")
lines = f.readlines()
# 存储路径
paths = []
for line in lines:
    # string类型数组转int型数组
    arr = list(map(int, line[1:-2].split(',')))
    paths.append(arr)
f.close()

for path in paths:
    length = 0
    print(path)

# 获取节点旁基站
tel_list = []
for path in paths:
    tel_list_ = []
    for node in path:
        # print(node)
        # print(df_re.loc[int(node)]['tel '])
        # 如果node旁边没有基站
        if len(df_re.loc[node]['tel']) == 2:
            # print(df_re.loc[int(node)]['tel'])
            # print('null')
            tel_list_.append([-1])
        else:
            # string类型数组转int型数组
            arr = list(map(int, df_re.loc[int(node)]['tel'][1:-2].split(',')))
            # print(df_re.loc[int(node)]['tel'])
            tel_list_.append(arr)
    tel_list.append(tel_list_)
# print(tel_list)

data = []
delay_file = str(configuration.TASK_SIZE)+'_'+str(configuration.CPU_CLOCK)+'time_delay.txt'
dijkstra_delay = 0
random_delay = 0
rl_based_delay = 0
for idx in range(10):
    data_line = []
    # ①迪杰斯特拉
    # 获得最近基站
    # print(paths)
    # print(df_tel.loc[1])
    dijkstra_choose_tel_list = []
    for i in range(len(paths)):
        dijkstra_choose_tel = []
        for j in range(len(paths[i])):
            if tel_list[i][j][0] == -1:
                dijkstra_choose_tel.append(-1)
            else:
                for tel in tel_list[i][j]:
                    if len(tel_list[i][j]) == 1 and df_tel[df_tel['index'].isin([tel])].empty:
                        dijkstra_choose_tel.append(-1)
                    elif df_tel[df_tel['index'].isin([tel])].empty:
                        dijkstra_choose_tel.append(-1)
                    else:
                        temp = 999999
                        distance = tools.geodistance(df_co.loc[paths[i][j]]['lon'], df_co.loc[paths[i][j]]['lat'],
                                                     df_tel.loc[df_tel.loc[df_tel['index'] == tel].index[0]]['lon'],
                                                     df_tel.loc[df_tel.loc[df_tel['index'] == tel].index[0]]['lat'])
                        if distance < temp:
                            temp = distance
                            if len(tel_list[i][j]) != 1 and not df_tel[df_tel['index'].isin([tel])].empty and tel != tel_list[i][j][0]:
                                # print(tel)
                                # print(tel_list[i][j][0])
                                # print(dijkstra_choose_tel)
                                dijkstra_choose_tel.pop()
                            dijkstra_choose_tel.append(tel)
        dijkstra_choose_tel_list.append(dijkstra_choose_tel)
    # print(dijkstra_choose_tel_list)

    dijkstra_transfer_sum = 0
    dijkstra_queue_sum = 0
    dijkstra_process_sum = 0
    dijkstra_delay_sum = 0
    dijkstra_count = 0
    for i in range(len(paths)):
        for j in range(len(paths[i])):
            # print(i, j)
            if dijkstra_choose_tel_list[i][j] == -1:
                transfer_time = configuration.TASK_SIZE / (
                        20 * math.log(1 + (configuration.VEHICLE_POWER * (127 + 30 * math.log(300, 10))) / 0.002,
                                      2)) * 1000
                queue_time = random.randint(10, 1000)
                process_time = configuration.TASK_SIZE / configuration.CPU_CLOCK
                tel_delay = transfer_time + queue_time + process_time

                dijkstra_transfer_sum += transfer_time
                dijkstra_queue_sum += queue_time
                dijkstra_process_sum += process_time
                dijkstra_delay_sum += tel_delay
                dijkstra_count += 1
            else:
                # dijkstra_choose_tel_list[i][j]
                distance = tools.geodistance(df_co.loc[paths[i][j]]['lon'], df_co.loc[paths[i][j]]['lat'],
                                             df_tel.loc[df_tel.loc[df_tel['index'] == dijkstra_choose_tel_list[i][j]].index[0]]['lon'],
                                             df_tel.loc[df_tel.loc[df_tel['index'] == dijkstra_choose_tel_list[i][j]].index[0]]['lat'])
                print(distance)
                transfer_speed = 20 * math.log(1 + (0.5 * (127 + 30 * math.log(distance, 10))) / 0.002, 2)
                transfer_time = configuration.TASK_SIZE / transfer_speed * 1000
                # 最近优先会导致队列延迟增大
                queue_time = choose_tel.get_real_queue(df_tel, tel)
                # np.random.seed(dijkstra_choose_tel_list[i][j])
                # process_speed = np.random.randint(10, 25)
                process_speed = configuration.CPU_CLOCK
                process_time = configuration.TASK_SIZE / process_speed
                tel_delay = transfer_time + queue_time + process_time

                dijkstra_transfer_sum += transfer_time
                dijkstra_queue_sum += queue_time
                dijkstra_process_sum += process_time
                dijkstra_delay_sum += tel_delay
                dijkstra_count += 1
    dijkstra_transfer_avg = dijkstra_transfer_sum / dijkstra_count
    dijkstra_queue_avg = dijkstra_queue_sum / dijkstra_count
    dijkstra_process_avg = dijkstra_process_sum / dijkstra_count
    dijkstra_delay_avg = dijkstra_delay_sum / dijkstra_count
    print("dijkstra_transfer_avg:", dijkstra_transfer_avg, "dijkstra_queue_avg:", dijkstra_queue_avg,
          "dijkstra_process_avg:", dijkstra_process_avg, "dijkstra_delay_avg:", dijkstra_delay_avg)
    with open(delay_file, "a") as f:
        line_one = "task_size:"+str(configuration.TASK_SIZE)+" cpu_clock:"+str(configuration.CPU_CLOCK)
        line_two = "dijkstra_transfer_avg:"+str(dijkstra_transfer_avg)+" dijkstra_queue_avg:"+str(dijkstra_queue_avg)+\
                   " dijkstra_process_avg:"+str(dijkstra_process_avg)+" dijkstra_delay_avg:"+str(dijkstra_delay_avg)
        f.write(line_one)
        f.write('\n')
        f.write(line_two)
        f.write('\n')
    data_line.append(str(dijkstra_transfer_avg))
    data_line.append(str(dijkstra_queue_avg))
    data_line.append(str(dijkstra_process_avg))
    data_line.append(str(dijkstra_delay_avg))
    dijkstra_delay += dijkstra_delay_avg

    # ②随机选择基站
    random_choose_tel_list = []
    for i in range(len(paths)):
        random_choose_tel = []
        for j in range(len(paths[i])):
            if tel_list[i][j][0] == -1:
                random_choose_tel.append(-1)
            else:
                tel = random.choice(tel_list[i][j])
                if df_tel[df_tel['index'].isin([tel])].empty:
                    tel = -1
                # distance = tools.geodistance(df_co.loc[paths[i][j]]['lon'], df_co.loc[paths[i][j]]['lat'],
                #                              df_tel.loc[tel]['lon'], df_tel.loc[tel]['lat'])
                # print(tel)
                random_choose_tel.append(tel)
        random_choose_tel_list.append(random_choose_tel)

    random_transfer_sum = 0
    random_queue_sum = 0
    random_process_sum = 0
    random_delay_sum = 0
    random_count = 0
    for i in range(len(paths)):
        for j in range(len(paths[i])):
            if random_choose_tel_list[i][j] == -1:
                transfer_time = configuration.TASK_SIZE / (
                        20 * math.log(1 + (configuration.VEHICLE_POWER * (127 + 30 * math.log(300, 10))) / 0.002,
                                      2)) * 1000
                queue_time = random.randint(10, 1500)
                process_time = configuration.TASK_SIZE / configuration.CPU_CLOCK
                tel_delay = transfer_time + queue_time + process_time

                random_transfer_sum += transfer_time
                random_queue_sum += queue_time
                random_process_sum += process_time
                random_delay_sum += tel_delay
                random_count += 1
            else:
                # random_choose_tel_list[i][j]
                distance = tools.geodistance(df_co.loc[paths[i][j]]['lon'], df_co.loc[paths[i][j]]['lat'],
                                             df_tel.loc[df_tel.loc[df_tel['index'] == random_choose_tel_list[i][j]].index[0]]['lon'],
                                             df_tel.loc[df_tel.loc[df_tel['index'] == random_choose_tel_list[i][j]].index[0]]['lat'])
                transfer_speed = 20 * math.log(1 + (0.5 * (127 + 30 * math.log(distance, 10))) / 0.002, 2)
                transfer_time = configuration.TASK_SIZE / transfer_speed * 1000
                # 随机算法会导致队列延迟增大
                queue_time = choose_tel.get_real_queue(df_tel, tel)
                process_speed = configuration.CPU_CLOCK
                process_time = configuration.TASK_SIZE / process_speed
                tel_delay = transfer_time + queue_time + process_time

                random_transfer_sum += transfer_time
                random_queue_sum += queue_time
                random_process_sum += process_time
                random_delay_sum += tel_delay
                random_count += 1
    random_transfer_avg = random_transfer_sum / random_count
    random_queue_avg = random_queue_sum / random_count
    random_process_avg = random_process_sum / random_count
    random_delay_avg = random_delay_sum / random_count
    print("random_transfer_avg:", random_transfer_avg, "random_queue_avg:", random_queue_avg,
          "random_process_avg:", random_process_avg, "random_delay_avg:", random_delay_avg)
    with open(delay_file, "a") as f:
        line_two = "random_transfer_avg:" + str(random_transfer_avg) + " random_queue_avg:" + str(
            random_queue_avg) + \
                   " random_process_avg:" + str(random_process_avg) + " random_delay_avg:" + str(random_delay_avg)
        f.write(line_two)
        f.write('\n')
    data_line.append(str(random_transfer_avg))
    data_line.append(str(random_queue_avg))
    data_line.append(str(random_process_avg))
    data_line.append(str(random_delay_avg))
    random_delay += random_delay_avg

    # ③RL-Based路径规划算法
    def check(q_table, df_re, start_point):
        current_point = start_point
        path = []
        try:
            for j in range(len(q_table)):
                # 路径数组
                path.append(current_point)

                # 根据node_id获得其value值 返回Series
                action_list = q_table.loc[str(current_point)]

                # 返回q_table中value值最大的索引
                action = action_list.astype(float).idxmax()

                c = current_point

                next_point = df_re.iloc[current_point, (int(action) - 1) * 5 + 1]

                current_point = int(next_point)
                if int(next_point) == end_point:
                    path.append(end_point)
                    break
        except:
            print('---------------------')
            print(start_point, '------>', end_point)
            print('current point is', current_point)
            print('action is', action)
            print('next point is', next_point)
            print('path is', path)
            traceback.print_exc()
        if end_point not in path:
            print(path)
            print(start_point, '----->', end_point, 'not contain end_point')

        return path


    # error_point = [750, 240, 189, 155, 199, 485, 306, 457, 380, 626, 116, 461]
    error_point = [301, 240, 306, 380, 626, 461, 34]
    rl_based_path = []
    for i in range(166, 288):
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        if start_point in error_point:
            continue
        end_point = np.random.randint(801, 1725)
        table_file_path = os.getcwd() + "/table/" + configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_q_table.csv'
        q_table = pd.read_csv(table_file_path, encoding='utf-8')
        q_table.set_index('Unnamed: 0', inplace=True)

        path_1 = check(q_table, df_re, start_point)
        rl_based_path.append(path_1)
    # print(rl_based_path)

    rl_tel_list = []
    for path in rl_based_path:
        rl_tel_list_ = []
        for node in path:
            # 如果node旁边没有基站
            if len(df_re.loc[node]['tel']) == 2:
                rl_tel_list_.append([-1])
            else:
                # string类型数组转int型数组
                arr = list(map(int, df_re.loc[int(node)]['tel'][1:-2].split(',')))
                rl_tel_list_.append(arr)
        rl_tel_list.append(rl_tel_list_)

    # 选择基站
    rl_based_choose_tel_list = []
    for i in range(len(rl_based_path)):
        rl_based_choose_tel = []
        for j in range(len(rl_based_path[i])):
            if rl_tel_list[i][j][0] == -1:
                rl_based_choose_tel.append(-1)
            else:
                tel = rl_tel_list[i][j][rl_based_path[i][j] % len(rl_tel_list[i][j])]
                if df_tel[df_tel['index'].isin([tel])].empty:
                    tel = -1
                rl_based_choose_tel.append(tel)
                # print(tel)
        rl_based_choose_tel_list.append(rl_based_choose_tel)

    rl_based_transfer_sum = 0
    rl_based_queue_sum = 0
    rl_based_process_sum = 0
    rl_based_delay_sum = 0
    rl_based_count = 0
    for i in range(len(rl_based_path)):
        for j in range(len(rl_based_path[i])):
            if rl_based_choose_tel_list[i][j] == -1:
                transfer_time = configuration.TASK_SIZE / (
                        20 * math.log(1 + (configuration.VEHICLE_POWER * (127 + 30 * math.log(300, 10))) / 0.002,
                                      2)) * 1000
                queue_time = random.randint(10, 1500)
                process_time = configuration.TASK_SIZE / configuration.CPU_CLOCK
                tel_delay = transfer_time + queue_time + process_time

                rl_based_transfer_sum += transfer_time
                rl_based_queue_sum += queue_time
                rl_based_process_sum += process_time
                rl_based_delay_sum += tel_delay
                rl_based_count += 1
            else:
                # rl_based_choose_tel_list[i][j]
                distance = tools.geodistance(df_co.loc[rl_based_path[i][j]]['lon'], df_co.loc[rl_based_path[i][j]]['lat'],
                                             df_tel.loc[df_tel.loc[df_tel['index'] == rl_based_choose_tel_list[i][j]].index[0]]['lon'],
                                             df_tel.loc[df_tel.loc[df_tel['index'] == rl_based_choose_tel_list[i][j]].index[0]]['lat'])
                transfer_speed = 20 * math.log(1 + (0.5 * (127 + 30 * math.log(distance, 10))) / 0.002, 2)
                transfer_time = configuration.TASK_SIZE / transfer_speed * 1000

                queue_time = choose_tel.get_real_queue(df_tel, tel)
                process_speed = configuration.CPU_CLOCK
                process_time = configuration.TASK_SIZE / process_speed
                tel_delay = transfer_time + queue_time + process_time

                rl_based_transfer_sum += transfer_time
                rl_based_queue_sum += queue_time
                rl_based_process_sum += process_time
                rl_based_delay_sum += tel_delay
                rl_based_count += 1
    rl_based_transfer_avg = rl_based_transfer_sum / rl_based_count
    rl_based_queue_avg = rl_based_queue_sum / rl_based_count
    rl_based_process_avg = rl_based_process_sum / rl_based_count
    rl_based_delay_avg = rl_based_delay_sum / rl_based_count
    print("rl_based_transfer_avg:", rl_based_transfer_avg, "rl_based_queue_avg:", rl_based_queue_avg,
          "rl_based_process_avg:", rl_based_process_avg, "rl_based_delay_avg:", rl_based_delay_avg)
    with open(delay_file, "a") as f:
        line_two = "rl_based_transfer_avg:" + str(rl_based_transfer_avg) + " rl_based_queue_avg:" + str(
            rl_based_queue_avg) + \
                   " rl_based_process_avg:" + str(rl_based_process_avg) + " rl_based_delay_avg:" + str(rl_based_delay_avg)
        f.write(line_two)
        f.write('\n')
        f.write('\n')
    data_line.append(str(rl_based_transfer_avg))
    data_line.append(str(rl_based_queue_avg))
    data_line.append(str(rl_based_process_avg))
    data_line.append(str(rl_based_delay_avg))
    data.append(data_line)
    rl_based_delay += rl_based_delay_avg
df_data = pd.DataFrame(data, columns=('dijkstra_transfer_avg', 'dijkstra_queue_avg:', 'dijkstra_process_avg', 'dijkstra_delay_avg',
                                          'random_transfer_avg', 'random_queue_avg', 'random_process_avg', 'random_delay_avg',
                                          'rl_based_transfer_avg', 'rl_based_queue_avg', 'rl_based_process_avg', 'rl_based_delay_avg'))
df_data.to_csv(os.path.dirname(os.getcwd()) + "/dataset/" + str(configuration.TASK_SIZE)+'_'+str(configuration.CPU_CLOCK)+'time_delay.csv', encoding='utf-8')
print('dijkstra_delay', dijkstra_delay/10, 'random_delay', random_delay/10, 'rl_based_delay', rl_based_delay/10)
