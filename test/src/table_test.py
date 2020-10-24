import configuration
import os
import pandas as pd
import numpy as np
import folium


if __name__ == '__main__':

    for i in range(166, 288):
        # 随机种子，保证和第一次训练是相同的
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        end_point = np.random.randint(801, 1725)
        table_file_path = os.getcwd() + "/table/" + configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_' + 'q_table.csv'

        relation_file_path = os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_relation.csv'

        node_info_file_path = os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_info_.csv'

        q_table = pd.read_csv(table_file_path, encoding='utf-8')
        q_table.set_index('Unnamed: 0', inplace=True)

        df_re = pd.read_csv(relation_file_path, encoding='utf-8')

        df_co = pd.read_csv(node_info_file_path, encoding='utf-8')

        current_point = start_point
        path = []
        while(True):
            try:
                # 路径数组
                path.append(current_point)
                print(current_point)

                # 根据node_id获得其value值 返回Series
                action_list = q_table.loc[str(current_point)]

                # 返回q_table中value值最大的索引
                action = action_list.astype(float).idxmax()

                next_point = df_re.iloc[current_point, (int(action)-1)*5+1]

                current_point = int(next_point)

                if int(next_point) == end_point:
                    path.append(end_point)
                    break
            except:
                break

        # 画图部分
        m = folium.Map([31.7750817, 117.3165301], zoom_start=15)
        for node in path:
            coordinate = [df_co.iloc[node, 2], df_co.iloc[node, 1]]
            folium.Marker(
                location=coordinate,
                fill_color='＃43d9de',
                radius=8
            ).add_to(m)
        #     os.getcwd() + "/table/" + configuration.CITY + '_' + str(
        #     configuration.START_POINT) + '_' + str(configuration.END_POINT) + '_' + 'q_table.csv'
        m.save(os.path.join(r'' + os.getcwd() + '/path/', configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_public_relation.html'))





