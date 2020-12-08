import numpy as np
import pandas as pd
import configuration
import os
import traceback


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
    # if end_point not in path:
        # print(path)
        # print(start_point, '----->', end_point, 'not contain end_point')

    return path


if __name__ == '__main__':
    error_point = [750, 240, 189, 155, 199, 485, 306, 457, 380, 626, 116, 461]
    count = 0
    for i in range(166, 288):
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        if start_point in error_point:
            continue
        end_point = np.random.randint(801, 1725)

        static_file_path = os.getcwd() + "/table/" + configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_q_table.csv'
        realtime_file_path = os.getcwd() + '/table_realtime_ts_' + str(configuration.TASK_SIZE) + '_cc_' + str(
            configuration.CPU_CLOCK) + '_vp_' + str(configuration.VEHICLE_POWER) + '/' + configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_realtime_q_table.csv'

        relation_file_path = os.path.dirname(
            os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv'

        node_info_file_path = os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_info_.csv'

        q_table = pd.read_csv(realtime_file_path, encoding='utf-8')
        q_table.set_index('Unnamed: 0', inplace=True)

        q_table_realtime = pd.read_csv(realtime_file_path, encoding='utf-8')
        q_table_realtime.set_index('Unnamed: 0', inplace=True)

        df_re = pd.read_csv(relation_file_path, encoding='utf-8')

        df_co = pd.read_csv(node_info_file_path, encoding='utf-8')

        path_1 = check(q_table, df_re, start_point)
        path_2 = check(q_table_realtime, df_re, start_point)

        if end_point in path_2 and path_1 != path_2:
            count += 1
            print('--------------------------')
            print(start_point, '---->', end_point)
            print(path_1)
            print(path_2)
            print('count:', count)
            print('**************************')
