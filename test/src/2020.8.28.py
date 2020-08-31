import json
import os
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import folium


import cross as cr
import tools

f = 1000000


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
def get_coordinate(way_info):
    coordinate = []
    for ele in way_info[2:]:
        _coordinate = []
        _coordinate.append(way_info[0])
        _coordinate.append(way_info[1])
        _coordinate.append(ele)
        _coordinate.append(round(coordinate_df.loc[int(ele)].loc['lon'], 6))
        _coordinate.append(round(coordinate_df.loc[int(ele)].loc['lat'], 6))
        coordinate.append(_coordinate)
    return coordinate

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
# 31.055399800000004,121.77162299999999
# 31.0562038,121.77168780000001


def cross(coordinate_info):
    index = 0
    cross_coordinate = []
    for single_road in coordinate_info:
        road_name = single_road[0][1]
        for i in range(len(single_road)-1):
            for _single_road in coordinate_info:
                if road_name == _single_road[0][1]:
                    continue
                else:
                    for j in range(i+1, len(_single_road)-1):
                        A = cr.Point(single_road[i][3]*f, single_road[i][4]*f)
                        B = cr.Point(single_road[i+1][3]*f, single_road[i+1][4]*f)
                        C = cr.Point(_single_road[j][3]*f, _single_road[j][4]*f)
                        D = cr.Point(_single_road[j+1][3]*f, _single_road[j+1][4]*f)
                        # 判断是否相交
                        if cr.is_intersected(A, B, C, D):
                            # 求交点坐标
                            cross_coordinate.append(cr.get_intersection(A, B, C, D))
                            index += 1
                            print(index)
                        j += 1
            i += 1
    return cross_coordinate


if __name__ == "__main__":
    way_ref = []  # 所有way的reference
    way_tuple = get_road()
    way_info = get_way_ref(way_tuple)
    coordinate_info = []

    coordinate_file = os.path.dirname(os.getcwd()) + "/dataset/id_coordinate.csv"
    coordinate_data = pd.read_csv(coordinate_file)
    coordinate_df = pd.DataFrame(coordinate_data)
    coordinate_df.set_index(['ref'], inplace=True)
    # print(coordinate_df)
    for ele in way_info:
        _coordiante_info = []
        _coordiante_info = get_coordinate(ele)
        coordinate_info.append(_coordiante_info)
    cross_coordinate = cross(coordinate_info)
    print(len(cross_coordinate))
    s = set(np.array(cross_coordinate))
    print(len(s))

    map = folium.Map([31.055, 121.771], zoom_start=18)
    map = tools.draw_node(map, cross_coordinate)
    map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', '十字路口.html'))
    # for single_road in coordinate_info:
    #     # print(len(single_road))
    #     folium.Marker(
    #         location=[single_road[len(single_road)-1][3], single_road[len(single_road)-1][4]],
    #         fill_color='＃43d9de',
    #         radius=8
    #     ).add_to(map)
    #     folium.Marker(
    #         location=[single_road[len(single_road)-1][3], single_road[len(single_road)-1][4]],
    #         fill_color='＃43d9de',
    #         radius=8
    #     ).add_to(map)
    # columns = ['ref', 'lon', 'lat', 'way_id', 'name']
    # save_file = pd.DataFrame(columns=columns, data=coordinate)
    # save_file.to_csv('id_coordinate.csv', index=False, encoding="utf-8")

