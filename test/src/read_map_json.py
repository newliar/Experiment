import json
import os
import numpy as np
import folium
import draw_node_test
import pandas as pd
import copy
from math import radians, cos, sin, asin, sqrt
from DFS import Dfs
import matplotlib.pyplot as plt

inf = float("inf")


def get_road():
    file_path = os.path.dirname(os.getcwd()) + "/dataset/allways.json"
    # print(file_path)
    file = open(file_path, 'r', encoding='utf-8')
    # 存放 干线公路、一级道路、二级道路、三级道路
    # trunk = []
    primary = []
    secondary = []
    tertiary = []
    unclassified = []
    residential = []
    # 存放道路连接路
    # trunk_link = []
    # primary_link = []
    # secondary_link = []
    # tertiary_link = []
    #  将道路存放到对应的list
    for line in file.readlines():
        dic = json.loads(line)
        # print(dic)
        if "tag" in dic:
            if isinstance(dic["tag"], list):
                for m in dic["tag"]:
                    # if m["v"] == "trunk":
                    #     trunk.append(dic)
                    #     break
                    if m["k"] == "highway" and m["v"] == "primary":
                        primary.append(dic)
                        break
                    if m["k"] == "highway" and m["v"] == "secondary":
                        secondary.append(dic)
                        break
                    if m["k"] == "highway" and m["v"] == "tertiary":
                        tertiary.append(dic)
                        break
                    if m["k"] == "highway" and m["v"] == "unclassified":
                        unclassified.append(dic)
                        break
                    if m["k"] == "highway" and m["v"] == "residential":
                        residential.append(dic)
                        break
                    # if m["v"] == "trunk_link":
                    #     trunk_link.append(dic)
                    #     break
                    # if m["v"] == "primary_link":
                    #     primary_link.append(dic)
                    #     break
                    # if m["v"] == "secondary_link":
                    #     secondary_link.append(dic)
                    #     break
                    # if m["v"] == "tertiary_link":
                    #     tertiary_link.append(dic)
                    #     break
            # elif dic["tag"]["v"] == "trunk":
            #     trunk.append(dic)
            # elif dic["tag"]["v"] == "primary":
            #     primary.append(dic)
            # elif dic["tag"]["v"] == "secondary":
            #     secondary.append(dic)
            # elif dic["tag"]["v"] == "tertiary":
            #     tertiary.append(dic)
            # elif dic["tag"]["v"] == "trunk_link":
            #     trunk_link.append(dic)
            # elif dic["tag"]["v"] == "primary_link":
            #     primary_link.append(dic)
            # elif dic["tag"]["v"] == "secondary_link":
            #     secondary_link.append(dic)
            # elif dic["tag"]["v"] == "tertiary_link":
            #     tertiary_link.append(dic)
    return primary, secondary, tertiary, unclassified, residential


# 获得道路的所有ref值
def get_way_ref(way):
    # 存储way的ref值
    way_ref = []
    way_refs = []
    for ele in way:
        temp = []
        for nd_ele in ele["nd"]:
            for value in nd_ele.values():
                temp.append(value)
                way_refs.append(value)
        way_ref.append(temp)
    return way_ref, way_refs


# 获得所有node之间的连接情况
def get_node_relation(node_relation, node_list, way_ref):
    # 存储各个ref的连通状态
    for way_kind in way_ref:
        for way in way_kind:
            for reference in way:
                # 矩阵对角线置1 节点与自身视为连通
                index_i = node_list.index(reference)
                # node_relation[index_i][index_i] = inf
                # 排除下标为0特殊情况
                if way.index(reference) == 0:
                    continue
                # 获得当前节点位于那一条way上
                else:
                    index_j = node_list.index(way[way.index(reference) - 1])
                    node_relation[index_i][index_j] = 1
                    node_relation[index_j][index_i] = 1
    return node_relation


# # 获得ref的不重复个数和道路的不重复集合
# def get_count(way_list):
#     # 获得ref的总数量
#     count = 0
#     count_1 = 0
#     # list类型
#     node_list = []
#     for m in way_list:
#         for n in m:
#             if n not in node_list:
#                 node_list.append(n)
#                 count += 1
#             count_1 += 1
#     print(count)
#     # print(way_list)
#     return count, node_list


# 获得ref在way_list的层数，即判断ref是不是同一条路上的点
def which_floor(way_list, ele):
    # i代表层数 flag跳出外层循环
    i = 1
    flag = 0
    for m in way_list:
        for n in m:
            if n == ele:
                flag = 1
                break
        if flag == 1:
            break
        i += 1
    return i


# 获得ref的经纬度
def get_coordinate(node_list, location):
    file_path = os.path.dirname(os.getcwd()) + "/dataset/node.json"
    file = open(file_path, 'r', encoding='utf-8')
    for line in file.readlines():
        dic = json.loads(line)
        if "id" in dic:
            if dic["id"] in node_list:
                if "lat" in dic and "lon" in dic:
                    index = node_list.index(dic["id"])
                    location[index, 0] = np.float64(dic["lon"])
                    location[index, 1] = np.float64(dic["lat"])
        else:
            continue
    return location


def get_distance(node_relation, location, distance_matrix):
    i = 0
    for line in node_relation:
        j = 0
        for ele in line:
            if ele == 1 and i != j:
                distance_matrix[i, j] = geodistance(location[i][0], location[i][1], location[j][0], location[j][1])
            j += 1
        i += 1
    return distance_matrix


def geodistance(lng1, lat1, lng2, lat2):
    # lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance, 3)
    return distance


def draw_node(map, location):
    for coordinate in location:
        folium.Marker(
            location=coordinate,
            fill_color='＃43d9de',
            radius=8
        ).add_to(map)
        print(coordinate)
    return map


if __name__ == "__main__":
    map = folium.Map([31.2329298, 121.4822705], zoom_start=10)
    node_set = set()  # 所有node的集合
    way_ref = []  # 所有way的reference
    # 获得所有的道路集合（元组）
    way_tuple = get_road()
    # 获得所有道路节点的不重复数量
    for way in way_tuple:
        way_ref.append(get_way_ref(way)[0])
        node_set = node_set | set(get_way_ref(way)[1])
    # 所有node的不重复数
    count = len(node_set)
    node_list = list(node_set)
    # 存储所有node的连接关系
    # 矩阵元素0代表不连通 1代表连通
    node_relation = np.zeros((count, count))

    distance_matrix = np.zeros((count, count))
    location = np.zeros([count, 2])
    # 获得各个节点的连通情况
    node_relation = get_node_relation(node_relation, node_list, way_ref)
    # 获得各个节点的经纬度及距离情况
    location = get_coordinate(node_list, location)
    for i in range(3620):
        plt.scatter(location[i, 0], location[i, 1], s=1, c='red')
    plt.show()
    plt.savefig("all_node.svg", format="svg")
    # df = pd.DataFrame(location)
    # df.columns = ['lon', 'lat']
    # df.to_csv('coordinate.csv', index=False)
    # distance_matrix = get_distance(node_relation.astype(int), location, distance_matrix)
    # x = np.nonzero(distance_matrix)
    #
    # a = np.zeros(count).astype(int)
    # dfs = Dfs(node_relation, a)

    # pd_data = pd.DataFrame(distance_matrix, columns=['node_x', 'node_y'])
    # print(pd_data)
    # pd_data.to_csv('F:/Experiment/test/dataset/pd_data.csv')
    # ---------------------------------------------------------------------------------

    # 打印单个 测试用
    # way_ref = get_way_ref(way_tuple[0])
    # way_info = get_node_relation(way_ref)
    # # print(type(way_ref))
    # location_map = draw_node_test.get_coordinate_test(way_info[0])
    # map = draw_node_test.get_way_node(map, way_ref, location_map)
    # print(way_ref)

    # 打印所有
    # for way in way_tuple:
    #     way_ref = get_way_ref(way)
    #     way_info = get_node_relation(way_ref)
    #     # print(way_info[0])
    #     # print(type(way_ref))
    #     location_map = draw_node_test.get_coordinate_test(way_info[0])
    #     map = draw_node_test.get_way_node(map, way_ref, location_map)

    # 画成地图并以网页存储
    # draw_node(map, location)
    # map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'primary_node.html'))
