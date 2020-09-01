import json
import os
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import folium


import cross as cr
import tools
import configuration as conf


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


# 获得ref的经纬度
# 返回值为3维表格
# 最里层表格列名分别为way_id, 道路名称, node_id, 经度, 纬度
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


# 根据经纬度计算两点之间距离
def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance, 3)
    return distance


# 得到路口信息
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
                        A = cr.Point(single_road[i][3]*conf.FACTOR, single_road[i][4]*conf.FACTOR)
                        B = cr.Point(single_road[i+1][3]*conf.FACTOR, single_road[i+1][4]*conf.FACTOR)
                        C = cr.Point(_single_road[j][3]*conf.FACTOR, _single_road[j][4]*conf.FACTOR)
                        D = cr.Point(_single_road[j+1][3]*conf.FACTOR, _single_road[j+1][4]*conf.FACTOR)
                        # 判断是否相交
                        if cr.is_intersected(A, B, C, D):
                            _cross_coordinate = []
                            # 求交点坐标
                            _cross_coordinate.append([single_road[i][0], single_road[i][1]])
                            _cross_coordinate.append([_single_road[j][0], _single_road[j][1]])
                            _cross_coordinate.append(cr.get_intersection(A, B, C, D))
                            cross_coordinate.append(_cross_coordinate)
                            index += 1
                            print(index)
                        j += 1
            i += 1
    return cross_coordinate


if __name__ == "__main__":
    # 根据osm文件获得所有道路信息
    way_tuple = get_road()
    way_info = get_way_ref(way_tuple)

    # 读取所有node节点的经纬度文件
    coordinate_file = os.path.dirname(os.getcwd()) + "/dataset/id_coordinate.csv"
    coordinate_data = pd.read_csv(coordinate_file)
    coordinate_df = pd.DataFrame(coordinate_data)
    coordinate_df.set_index(['ref'], inplace=True)

    coordinate_info = []
    # 获得所需道路上节点的经纬度
    for ele in way_info:
        coordinate_info.append(get_coordinate(ele))
    # 获得十字路口信息
    cross_coordinate = cross(coordinate_info)

    # 调用folium画图
    # map = folium.Map([31.055, 121.771], zoom_start=18)
    # map = tools.draw_node(map, cross_coordinate)
    # map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', '十字路口.html'))

