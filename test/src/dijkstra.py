import os
import numpy as np
import pandas as pd
import configuration


def startwith(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]: idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]: dis[i] = dis[idx] + mgraph[idx][i]
    print(passed)
    return dis


if __name__ == "__main__":
    # 读取文件  路口信息及连通关系和基站信息
    df_re = pd.read_csv(
        os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv',
        encoding='utf-8')
    df_co = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_node&tel.csv',
                        encoding='utf-8')

    df_tel = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_tel_station.csv',
                         encoding='utf-8')
    length = df_re.shape[0]
    # 构建邻接矩阵
    # inf = 99999999
    map_matrix = np.ones((length, length)) * np.inf
    for index, row in df_re.iterrows():
        # print(row['target_point_one'], row['target_point_two'], row['target_point_three'], row['target_point_four'])
        if bool(1 - pd.isna(row['target_point_one'])):
            map_matrix[index][int(row['target_point_one'])] = row['distance_one']

        if bool(1 - pd.isna(row['target_point_two'])):
            map_matrix[index][int(row['target_point_two'])] = row['distance_two']

        if bool(1 - pd.isna(row['target_point_three'])):
            map_matrix[index][int(row['target_point_three'])] = row['distance_three']

        if bool(1 - pd.isna(row['target_point_four'])):
            map_matrix[index][int(row['target_point_four'])] = row['distance_four']

    error_point = [750, 240, 189, 155, 199, 485, 306, 457, 380, 626, 116, 461]
    dis_list = []
    for i in range(166, 288):
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        if start_point in error_point:
            continue
        dis = startwith(start_point, map_matrix)
        dis_list.append(dis)
