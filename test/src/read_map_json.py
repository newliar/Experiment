import json
import os
import numpy as np


def get_road():
    file_path = os.path.dirname(os.getcwd()) + "/dataset/allways.json"
    # print(file_path)
    file = open(file_path, 'r', encoding='utf-8')
    # 存放 干线公路、一级道路、二级道路、三级道路
    trunk = []
    primary = []
    secondary = []
    tertiary = []
    # 存放道路连接路
    trunk_link = []
    primary_link = []
    secondary_link = []
    tertiary_link = []
    #  将道路存放到对应的list
    for line in file.readlines():
        dic = json.loads(line)
        # print(dic)
        if "tag" in dic:
            if isinstance(dic["tag"], list):
                for m in dic["tag"]:
                    if m["v"] == "trunk":
                        trunk.append(dic)
                        break
                    if m["v"] == "primary":
                        primary.append(dic)
                        break
                    if m["v"] == "secondary":
                        secondary.append(dic)
                        break
                    if m["v"] == "tertiary":
                        tertiary.append(dic)
                        break
                    if m["v"] == "trunk_link":
                        trunk_link.append(dic)
                        break
                    if m["v"] == "primary_link":
                        primary_link.append(dic)
                        break
                    if m["v"] == "secondary_link":
                        secondary_link.append(dic)
                        break
                    if m["v"] == "tertiary_link":
                        tertiary_link.append(dic)
                        break
            elif dic["tag"]["v"] == "trunk":
                trunk.append(dic)
            elif dic["tag"]["v"] == "primary":
                primary.append(dic)
            elif dic["tag"]["v"] == "secondary":
                secondary.append(dic)
            elif dic["tag"]["v"] == "tertiary":
                tertiary.append(dic)
            elif dic["tag"]["v"] == "trunk_link":
                trunk_link.append(dic)
            elif dic["tag"]["v"] == "primary_link":
                primary_link.append(dic)
            elif dic["tag"]["v"] == "secondary_link":
                secondary_link.append(dic)
            elif dic["tag"]["v"] == "tertiary_link":
                tertiary_link.append(dic)
    return trunk, primary, secondary, tertiary, trunk_link, primary_link, secondary_link, tertiary_link


# 获得道路的所有ref值
def get_way_ref(way):
    # 存储way的ref值
    way_ref = []
    for ele in way:
        temp = []
        for nd_ele in ele["nd"]:
            for value in nd_ele.values():
                temp.append(value)
        way_ref.append(temp)
    return way_ref


# 获得所有node之间的连接情况
def get_node_relation(way_list):
    # 获得count和node_relation(无重复点)
    dic = get_count(way_list)
    count = dic[0]
    node_list = dic[1]
    # print(count)
    # 存储各个ref的连通状态
    # 矩阵元素0代表不连通 1代表连通
    node_relation = np.zeros((count, count))
    for m in way_list:
        for n in m:
            # 矩阵对角线置1 节点与自身视为连通
            index = node_list.index(n)
            node_relation[index][index] = 1
            # 排除下标为0特殊情况
            if index == 0:
                continue
            # 获得当前节点位于那一条way上
            else:
                i = which_floor(way_list, n)
                j = which_floor(way_list, node_list[index - 1])
                # 同一条way上 相邻节点视为连通
                if i == j:
                    node_relation[index][index - 1] = 1
                    node_relation[index - 1][index] = 1

            # print(str(n)+"--------"+str(which_floor(way_list, n)))
    # print(node_list)
    return node_list, node_relation


# 获得ref的不重复个数和道路的不重复集合
def get_count(way_list):
    # 获得ref的总数量
    count = 0
    count_1 = 0
    # list类型
    node_list = []
    for m in way_list:
        for n in m:
            if n not in node_list:
                node_list.append(n)
                count += 1
            count_1 += 1
    # print(count)
    # print(way_list)
    return count, node_list


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
def get_coordinate(node_list):
    file_path = os.path.dirname(os.getcwd()) + "/dataset/node.json"
    file = open(file_path, 'r', encoding='utf-8')
    for line in file.readlines():
        dic = json.loads(line)
        if "id" in dic:
            if dic["id"] in node_list:
                if "lat" in dic and "lon" in dic:
                    print("node:" + str(dic["id"]) + "  " + "latitude:" + str(dic["lat"]) + "  " + "longitude:" + str(dic["lon"]))
        else:
            continue


if __name__ == "__main__":
    way_tuple = get_road()
    way_info = get_node_relation(get_way_ref(way_tuple[0]))
    # print(way_info[0])
    get_coordinate(way_info[0])
