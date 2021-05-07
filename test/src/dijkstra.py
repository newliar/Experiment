import os
import numpy as np
import pandas as pd
import configuration


def startwith(start: int, mgraph: list) -> list:
    # dist = mgraph[start]
    # dist[start] = 0
    # path = [0 for _ in range(len(mgraph))]
    # path[start] = -1
    # checked = [0 for _ in range(len(mgraph))]
    # while True:
    #     pass
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]
    print(dis)
    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]:
                idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]:
                dis[i] = dis[idx] + mgraph[idx][i]
                # seq = (path[idx], str(i))
                # print(seq)
                # sym = '-'
                # path[i] = sym.join(seq)  # 起始点到（当前点的相邻点k）的最短路径，以'-'来连接seq中的两个字符串
    return dis


def Dijkstra(mgraph: list, start: int, end: int):
    # start-end的最短路径
    path = []
    # 邻接矩阵维度，即节点个数
    n = len(mgraph)
    fmax = np.inf
    # 邻接矩阵转化成维度矩阵，即0→max
    w = [[0 for i in range(n)]for j in range(n)]
    # 是否已经是最小的标记列表
    book = [0 for i in range(n)]
    # start到其他节点的最小距离
    dis = [fmax for i in range(n)]
    # 节点编号从start开始，列表序号从0开始
    book[start] = 1
    # 上一跳列表
    midpath = [-1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if mgraph[i][j] != 0:
                # 0→max
                w[i][j] = mgraph[i][j]
            else:
                w[i][j] = fmax
            # 直连的节点最小距离就是network[i][j]
            if i == start and mgraph[i][j] != 0:
                dis[j] = mgraph[i][j]
    # n-1次遍历，除了start节点
    for i in range(n-1):
        min = fmax
        for j in range(n):
            # 如果未遍历且距离最小
            if book[j] == 0 and dis[j] < min:
                min = dis[j]
                u = j
        book[u] = 1
        # u直连的节点遍历一遍
        for v in range(n):
            if dis[v] > dis[u] + w[u][v]:
                dis[v] = dis[u] + w[u][v]
                midpath[v] = u+1
    # j是序号
    j = end
    # 因为存储的是上一跳，所以先加入目的节点d，最后倒置
    path.append(end)
    while midpath[j] != -1:
        path.append(midpath[j]-1)
        j = midpath[j] - 1
    path.append(start)
    path.reverse()

    print(path)
    print('length: ', len(path))
    with open("迪杰斯特拉路径.txt", "a") as f:
        f.write(str(path))
        f.write('\n')

    return dis
    # print(len(dis))


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

    # print(map_matrix)

    error_point = [512, 5, 138, 779, 280, 155, 34, 675, 420, 424, 301, 430, 306, 439, 701, 189, 317, 63, 322, 199,
                   457, 461, 589, 725, 215, 599, 345, 732, 351, 609, 485, 620, 240, 626, 380]
    dis_list = []
    s_e_d = []
    for i in range(166, 288):
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        end_point = np.random.randint(801, 1725)
        if start_point in error_point:
            continue
        print(start_point, end_point)
        dis = Dijkstra(map_matrix, start_point, end_point)
        s_e_d.append([start_point, end_point, dis[end_point]])
    distance_info = pd.DataFrame(s_e_d, columns=['start_point', 'end_point', 'distance'])
    distance_info.to_csv('./迪杰斯特拉距离.csv')


