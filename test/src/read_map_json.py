import json
import os
import numpy as np

def get_road():
    file_path = os.path.dirname(os.getcwd())+"/dataset/allways.json"
    print(file_path)
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
    return(trunk, primary, secondary, tertiary, trunk_link, primary_link, secondary_link, tertiary_link)

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
    # 获得ref的总数量
    count = 0
    count_1 = 0
    # list类型
    node_relation = []
    for m in way_list:
        for n in m:
            if n not in node_relation:
                node_relation.append(n)
                count += 1
            count_1 += 1
    print(count)
    print(count_1)

    # 存储各个ref的连通状态
    node_array = np.zeros([count, count])
    # i j是node_array下标
    i = 0
    for m in way_list:
        j = 0
        for n in m:
            index = node_relation.index(n)
            node_array[index][index] = 1
    print(node_array)


if __name__ == "__main__":
    way_tuple = get_road()
    get_node_relation(get_way_ref(way_tuple[0]))
