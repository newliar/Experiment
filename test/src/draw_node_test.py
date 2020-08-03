import os
import json
import folium
import numpy as np

# 31.2329298    121.4822705
m = folium.Map([31.2329298, 121.4822705], zoom_start=6)


# 获得ref的经纬度 可视化测试用
def get_coordinate_test(node_list):
    file_path = os.path.dirname(os.getcwd()) + "/dataset/node.json"
    file = open(file_path, 'r', encoding='utf-8')
    location_map = {}
    for line in file.readlines():
        dic = json.loads(line)
        if "id" in dic:
            if dic["id"] in node_list:
                if "lat" in dic and "lon" in dic:
                    coordinate = [np.float64(dic["lat"]), np.float64(dic["lon"])]
                    location_map[dic["id"]] = coordinate
        else:
            continue
    return location_map


# 获得所有的经纬度集合
def get_way_node(map, way_ref, location_map):
    all_location = []
    for m in way_ref:
        location = []
        for n in m:
            if n in location_map:
                location.append(location_map[n])
        all_location.append(location)
    # print(all_location)
    # map = draw_line(map, all_location)
    map = draw_node(map, all_location)
    return map


# 画出所有路线
def draw_line(map, all_location):
    for location in all_location:
        route = folium.PolyLine(
            location,
            weight=5,
            color='black',
            opacity=1
        ).add_to(map)
    return map
    # m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'node.html'))


# 画点
def draw_node(map, all_location):
    for location in all_location:
        for coordinate in location:
            folium.Marker(
                location=coordinate,
                fill_color='＃43d9de',
                radius=8
            ).add_to(map)
            print(coordinate)
    return map
