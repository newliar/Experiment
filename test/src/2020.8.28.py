import json
import os
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, sqrt


def get_road():
    file_path = os.path.dirname(os.getcwd()) + "/dataset/allways.json"
    file = open(file_path, 'r', encoding='utf-8')
    # 存放 干线公路、一级道路、二级道路、三级道路
    primary = []
    secondary = []
    tertiary = []
    unclassified = []
    residential = []
    for line in file.readlines():
        dic = json.loads(line)
        if "tag" in dic:
            if isinstance(dic["tag"], list):
                for m in dic["tag"]:
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
    return primary, secondary, tertiary, unclassified, residential


# 获得道路的所有ref值
def get_way_ref(way):
    # 存储way的ref值
    way_ref = []
    for way_type in way:
        for single_way in way_type:
            temp = []
            temp.append(single_way["id"])
            if isinstance(single_way["tag"], list):
                for ele in single_way["tag"]:
                    if ele["k"] == "name":
                        temp.append(ele["v"])
            for nodes in single_way["nd"]:
                for node_value in nodes.values():
                    temp.append(node_value)
            way_ref.append(temp)
    return way_ref


def delete_node(way, ref):

    pass


# 获得ref的经纬度,写成csv
def get_coordinate(way_info, coordinate_df):
    a = np.array(way_info)
    for ele in a[2:]:
        if ele in coordinate_df:
    #         在coordinate_df定位特定ref的行标

    # print(coordinate_df)
    # coordinate = []
    # for line in file.readlines():
    #     dic = json.loads(line)
    #     if "id" in dic:
    #         if dic["id"] in node_list:
    #             if "lat" in dic and "lon" in dic:
    #                 _coordinate = []
    #                 _coordinate.append(dic["id"])
    #                 _coordinate.append(np.float64(dic["lon"]))
    #                 _coordinate.append(np.float64(dic["lat"]))
    #                 coordinate.append(_coordinate)


# 根据经纬度计算两点之间距离
def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance, 3)
    return distance


if __name__ == "__main__":
    way_ref = []  # 所有way的reference
    way_tuple = get_road()
    way_info = get_way_ref(way_tuple)

    coordinate_file = os.path.dirname(os.getcwd()) + "/dataset/id_coordinate.csv"
    coordinate_data = pd.read_csv(coordinate_file)
    coordinate_df = pd.DataFrame(coordinate_data)
    for ele in way_info:
        get_coordinate()

    # columns = ['ref', 'lon', 'lat', 'way_id', 'name']
    # save_file = pd.DataFrame(columns=columns, data=coordinate)
    # save_file.to_csv('id_coordinate.csv', index=False, encoding="utf-8")

