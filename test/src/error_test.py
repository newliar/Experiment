# 检查那些个点不合法

import configuration
import os
import numpy as np
import pandas as pd
import traceback
import tools

# error_list = [485, 199, 457, 461, 750, 240, 306, 626, 116, 155, 380, 189]
# error_list = [34, 301, 461, 240, 306, 626, 380]
error_list = [512, 5, 138, 779, 280, 155, 34, 675, 420, 424, 301, 430, 306, 439, 701, 189, 317, 63, 322, 199,
              457, 461, 589, 725, 215, 599, 345, 732, 351, 609, 485, 620, 240, 626, 380]
node_info_file_path = os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_info_.csv'
node_info_list = pd.read_csv(node_info_file_path, encoding='utf-8').values.tolist()
print(node_info_list[0][1])
distance = 0
for i in range(166, 288):
    distance_ = 0
    # 随机种子，保证和第一次训练是相同的
    np.random.seed(i)
    start_point = np.random.randint(0, 800)
    if start_point in error_list:
        continue
    end_point = np.random.randint(801, 1725)

    # 读取第一次q_table和第二次q_table
    table_file_path = os.getcwd() + "/table_realtime_Ω_0.8_ts_100_cc_0.1_vp_0.7/" + configuration.CITY + '_' + str(
        start_point) + '_' + str(end_point) + '_realtime_q_table.csv'
    # os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.1_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
    # realtime_q_table = os.getcwd() + "/table_realtime_Ω_0.5_ts_100_cc_0.1_vp_666/" + configuration.CITY + '_' + str(
    #     start_point) + '_' + str(end_point) + '_realtime_q_table.csv'

    # 节点关系信息
    relation_file_path = os.path.dirname(
        os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv'

    # 节点信息

    # 转成dataframe格式
    q_table = pd.read_csv(table_file_path, encoding='utf-8')
    q_table.set_index('Unnamed: 0', inplace=True)

    # q_table_realtime = pd.read_csv(realtime_q_table, encoding='utf-8')
    # q_table_realtime.set_index('Unnamed: 0', inplace=True)

    df_re = pd.read_csv(relation_file_path, encoding='utf-8')

    # df_co = pd.read_csv(node_info_file_path, encoding='utf-8')

    current_point = start_point
    path = []
    try:
        for i in range(len(q_table)):
            # 路径数组
            path.append(current_point)

            # 根据node_id获得其value值 返回Series
            action_list = q_table.loc[str(current_point)]

            # 返回q_table中value值最大的索引
            action = action_list.astype(float).idxmax()

            c = current_point

            next_point = df_re.iloc[current_point, (int(action) - 1) * 5 + 1]

            temp = tools.geodistance(lonA=(node_info_list[int(c)][1]), latA=node_info_list[int(c)][2],
                                          lonB=node_info_list[int(next_point)][1], latB=node_info_list[int(next_point)][2])*1000
            distance+=temp

            current_point = int(next_point)
            if int(next_point) == end_point:
                path.append(end_point)
                break

    except:
        error_list.append(start_point)
        print('---------------------')
        print(start_point, '------>', end_point)
        print('current point is', current_point)
        print('action is', action)
        print('next point is', next_point)
        print('path is', path)
        traceback.print_exc()
    if end_point not in path:
        error_list.append(start_point)
        print(path)
        print(start_point, '----->', end_point, 'not contain end_point')
    # distance.append(distance_)

print(distance/85)
error_set = set(error_list)
print(len(error_set), error_set)
