import json
import os
import numpy as np
import pandas as pd
import folium

import cross as cr
import tools
import configuration as conf
import t_file
import configuration


def get_road():
    file_path = os.path.dirname(os.getcwd()) + "\\dataset\\"+configuration.CITY+"_ways.json"
    file = open(file_path, 'r', encoding='utf-8')
    # 存放 干线公路、一级道路、二级道路、三级道路
    trunk = []
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
                    # if (m["k"] == "bridge" and m["v"] == "yes") or (m["k"] == "layer" and m["v"] == "-1"):
                    #     break
                    # else:
                    if m["k"] == "highway" and m["v"] == "trunk":
                        trunk.append(dic)
                        break
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
    return trunk, primary, secondary, tertiary, unclassified, residential


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


def delete_node(cross_coordinate):
    coordinates_del = []
    coordinate_err = []
    for i in range(len(cross_coordinate) - 1):
        for j in range(i + 1, len(cross_coordinate)):
            distance = tools.geodistance(cross_coordinate[i][2][0], cross_coordinate[i][2][1],
                                         cross_coordinate[j][2][0], cross_coordinate[j][2][1])
            if distance < 40:
                print(distance)
                print(cross_coordinate[i])
                coordinates_del.append(cross_coordinate[i])
                break

    index = 1
    for coordinate in coordinates_del:
        # print(coordinate)
        try:
            cross_coordinate.remove(coordinate)
        except Exception as ex:
            coordinate_err.append(coordinate)
            print(coordinate)
            print("异常%s" % ex)
        else:
            # print("********************")
            # print("remove success+"+str(index))
            # print(coordinate)
            # print("********************")
            index += 1

    return cross_coordinate, coordinates_del, coordinate_err


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
        _coordinate.append(round(coordinate_df.loc[int(ele)].loc['lon'], 7))
        _coordinate.append(round(coordinate_df.loc[int(ele)].loc['lat'], 7))
        coordinate.append(_coordinate)
    return coordinate


# 得到路口信息
def cross(coordinate_info):
    index = 0
    cross_coordinate = []
    for single_road in coordinate_info:
        # road_name = single_road[0][1]
        road_id = single_road[0][0]
        for i in range(len(single_road) - 2):
            for _single_road in coordinate_info:
                # 重名路首尾连接不算路口
                # if road_name == _single_road[0][1]:
                if road_id == _single_road[0][0]:
                    continue
                else:
                    for j in range(i + 1, len(_single_road)):
                        if j == len(_single_road) - 1:
                            break
                        else:
                            A = cr.Point(single_road[i][3] * conf.FACTOR, single_road[i][4] * conf.FACTOR)
                            B = cr.Point(single_road[i + 1][3] * conf.FACTOR, single_road[i + 1][4] * conf.FACTOR)
                            C = cr.Point(_single_road[j][3] * conf.FACTOR, _single_road[j][4] * conf.FACTOR)
                            D = cr.Point(_single_road[j + 1][3] * conf.FACTOR, _single_road[j + 1][4] * conf.FACTOR)
                            # 判断是否相交
                            if cr.is_intersected(A, B, C, D):
                                _cross_coordinate = []
                                # 求交点坐标
                                _cross_coordinate.append([single_road[i][0], single_road[i][1]])
                                _cross_coordinate.append([_single_road[j][0], _single_road[j][1]])
                                _cross_coordinate.append(cr.get_intersection(A, B, C, D))
                                cross_coordinate.append(_cross_coordinate)
                                index += 1
                                # print(index)
                        j += 1
            i += 1
    return cross_coordinate


def get_way_order(way_tuple):
    way_name_arr = []
    way_order = []
    for way_type in way_tuple:
        for single_way in way_type:
            if isinstance(single_way["tag"], list):
                for ele in single_way["tag"]:
                    if ele["k"] == "name" and ele["v"] not in way_name_arr:
                        way_name_arr.append(ele["v"])
    for way_name in way_name_arr:
        order = []
        for way_type in way_tuple:
            for single_way in way_type:
                if isinstance(single_way["tag"], list):
                    for ele in single_way["tag"]:
                        if ele["k"] == "name" and ele["v"] == way_name:
                            order.append(single_way["id"])
        way_order.append(order)
    return way_name_arr, way_order


def get_public_node(way_info):
    all_node = []
    for way in way_info:
        for node in way[2:len(way)]:
            all_node.append(node)
    _public_node = []
    for node in all_node:
        public_node_ = [node]
        for way in way_info:
            for single_node in way[2:len(way)]:
                if node == single_node:
                    public_node_.append(way[0])
                    public_node_.append(way[1])
        _public_node.append(public_node_)
    public_node = []
    for ele in _public_node:
        if len(ele)>3:
            public_node.append(ele)
    return public_node


if __name__ == "__main__":
    # 根据osm文件获得所有道路信息
    way_tuple = get_road()
    # way_name, way_order = get_way_order(way_tuple)
    way_info = get_way_ref(way_tuple)
    # # 读取所有node节点的经纬度文件
    # coordinate_file = os.path.dirname(os.getcwd()) + "/dataset/id_coordinate.csv"
    # coordinate_data = pd.read_csv(coordinate_file)
    # coordinate_df = pd.DataFrame(coordinate_data)
    # coordinate_df.set_index(['ref'], inplace=True)
    # coordinate_info = []
    # # 获得所需道路上节点的经纬度
    # for ele in way_info:
    #     coordinate_info.append(get_coordinate(ele))
    # # 获得十字路口信息
    # cross_coordinate = cross(coordinate_info)
    # _cross_coordinate, coordinates_del, error = delete_node(cross_coordinate)
    # info, save_file = tools.write_cross_to_file(_cross_coordinate)
    # # 调用folium画图
    # m = folium.Map([31.2240060, 121.4639028], zoom_start=15)
    # m = tools.draw_node(m, _cross_coordinate)
    # m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'all_node.html'))



    # t_file.draw_node_by_name(coordinate_info)


    # 获得公共点
    public_node = get_public_node(way_info)
    coordinate_file = os.path.dirname(os.getcwd()) + "/dataset/"+configuration.CITY+"_id_coordinate.csv"
    coordinate_data = pd.read_csv(coordinate_file)
    coordinate_df = pd.DataFrame(coordinate_data)
    coordinate_df.set_index(['ref'], inplace=True)
    list_ = []
    for node_ in public_node:
        list_.append(coordinate_df.loc[int(node_[0])].tolist())
    df_node = pd.DataFrame(public_node,
                           columns=[
                               'node_id', 'way_id_one', 'way_name_one', 'way_id_two', 'way_name_two',
                               'way_id_three', 'way_name_three', 'way_id_four', 'way_name_four'
                               # 'way_id_five', 'way_name_five'
                           ])
    df_coor = pd.DataFrame(list_, columns=['lon', 'lat'])
    df = pd.concat([df_coor, df_node], axis=1)
    df.to_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_info.csv', index=True, encoding="utf-8")
    m = folium.Map([31.864183, 117.2939917], zoom_start=15)
    for location in list_:
        coordinate = [location[1], location[0]]
        folium.Marker(
            # folium格式，【纬度，经度】
            location=coordinate,
            fill_color='＃43d9de',
            radius=8
        ).add_to(m)
    m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', configuration.CITY+'_public_node.html'))

