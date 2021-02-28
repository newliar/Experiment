import configuration
import os
import pandas as pd
import numpy as np
import folium
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
    if end_point not in path:
        print(path)
        print(start_point, '----->', end_point, 'not contain end_point')

    return path


if __name__ == '__main__':
    # error_point = [256, 512, 768, 3, 5, 778, 138, 779, 655, 786, 789, 793, 155, 34, 675, 420, 293, 424, 169, 428, 301,
    #                173, 431, 49, 306, 182, 439, 701, 189, 65, 322, 199, 456, 457, 461, 725, 599, 345, 732, 734, 351,
    #                98, 485, 742, 104, 490, 620, 750, 240, 753, 626, 116, 380]
    error_point = [750, 240, 189, 155, 199, 485, 306, 457, 380, 626, 116, 461]
    count = 0
    for i in range(166, 288):
        # 随机种子，保证和第一次训练是相同的
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        if start_point in error_point:
            continue
        end_point = np.random.randint(801, 1725)
        table_file_path = os.getcwd() + "/table/" + configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_q_table.csv'
        # realtime_q_table = os.getcwd() + "/table_realtime/" + configuration.CITY + '_' + str(
        #     start_point) + '_' + str(end_point) + '_realtime_q_table.csv'

        relation_file_path = os.path.dirname(
            os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv'

        node_info_file_path = os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_info_.csv'

        q_table = pd.read_csv(table_file_path, encoding='utf-8')
        q_table.set_index('Unnamed: 0', inplace=True)

        # q_table_realtime = pd.read_csv(realtime_q_table, encoding='utf-8')
        # q_table_realtime.set_index('Unnamed: 0', inplace=True)

        df_re = pd.read_csv(relation_file_path, encoding='utf-8')

        df_co = pd.read_csv(node_info_file_path, encoding='utf-8')

        path_1 = check(q_table, df_re, start_point)
        print(path_1)
        # path_2 = check(q_table_realtime, df_re, start_point)
        #
        # if end_point in path_2 and path_1 != path_2:
        #     count += 1
        #     print('--------------------------')
        #     print(start_point, '---->', end_point)
        #     print(path_1)
        #     print(path_2)
        #     print('count:', count)
        #     print('**************************')

        # 画图部分
        # m = folium.Map([31.7750817, 117.3165301], zoom_start=10)
        # coordinate = []
        # for node in path_2:
        #     coordinate.append([df_co.iloc[node, 2], df_co.iloc[node, 1]])
        # folium.PolyLine(
        #     coordinate,
        #     color='blue',
        #     radius=8
        # ).add_to(m)
        # s_c = [df_co.iloc[path_2[0], 2], df_co.iloc[path_2[0], 1]]
        # e_c = [df_co.iloc[path_2[len(path_2)-1], 2], df_co.iloc[len(path_2)-1], 1]
        # folium.Marker(
        #     s_c,
        #
        # )
        #     os.getcwd() + "/table/" + configuration.CITY + '_' + str(
        #     configuration.START_POINT) + '_' + str(configuration.END_POINT) + '_' + 'q_table.csv'
        # m.save(os.path.join(r'' + os.getcwd() + '/path/', configuration.CITY + '_' + str(
        #     start_point) + '_' + str(end_point) + '_path.html'))
        # m.save(os.path.join(r'' + os.getcwd() + '/path_2th/', configuration.CITY + '_' + str(
        #     start_point) + '_' + str(end_point) + '_2th_path.html'))
