import matplotlib.pyplot as plt
import folium
import os
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt, atan2, degrees
from bs4 import BeautifulSoup
import random


# 画两条线段
def draw_line():
    plt.scatter(121.771594 * 1000000, 31.055035 * 1000000, color='red')
    plt.scatter(121.7716 * 1000000, 31.055103 * 1000000, color='red')
    # plt.scatter(121.737941*1000000, 31.042536*1000000, color='blue')
    # plt.scatter(121.737857*1000000, 31.042544*1000000, color='blue')


# draw_line()
# plt.show()
# plt.savefig("line.svg", format="svg")

def draw_node(m, all_location):
    for location in all_location:
        # 数据集格式【经度， 纬度】
        try:
            coordinate = [location[2][1], location[2][0]]
        except:
            print(location)
        else:
            folium.Marker(
                # folium格式，【纬度，经度】
                location=coordinate,
                fill_color='＃43d9de',
                radius=8
            ).add_to(m)
    return m


def get_all_node(coordinate_info):
    coordinate = []
    for ele_ in coordinate_info:
        for ele in ele_:
            coordinate.append([ele[3], ele[4]])
    return coordinate


def draw_relation(relation, cross_info):
    m = folium.Map([31.2240060, 121.4639028], zoom_start=15)
    for single_relation in relation:
        color = get_random_color()
        for ele in single_relation:
            location_1 = [cross_info[ele[0]][6], cross_info[ele[0]][5]]
            location_2 = [cross_info[ele[1]][6], cross_info[ele[1]][5]]
            location = [location_1, location_2]
            route = folium.PolyLine(
                location,
                weight=5,
                color='black',
                opacity=1
            ).add_to(m)
    m.add_child(folium.LatLngPopup())
    m.add_child(
        folium.ClickForMarker(popup='Waypoint')
    )
    # for ele in cross_info:
    #     coordinate = [ele[6], ele[5]]
    #     folium.Marker(
    #         # folium格式，【纬度，经度】
    #         location=coordinate,
    #         fill_color='＃43d9de',
    #         radius=8
    #     ).add_to(m)

    m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'relation_no_node.html'))


def get_random_color():
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0, 14)]
    return "#"+color


def write_cross_to_file(cross_coordinate):
    index = 0
    info = []
    for ele in cross_coordinate:
        info.append([ele[0][0], ele[0][1],
                     ele[1][0], ele[1][1],
                     round(ele[2][0], 7), round(ele[2][1], 7)])
        print(str(index) + ele[0][1])
        index += 1
    columns = ['way_one_id', 'way_one_name', 'way_two_id', "way_two_name", "lon", "lat"]
    save_file = pd.DataFrame(columns=columns, data=info)
    try:
        save_file.to_csv('cross_info.csv', index=True, encoding="utf-8")
    except:
        os.remove('cross_info.csv')
        try:
            save_file.to_csv('cross_info.csv', index=True, encoding="utf-8")
        except Exception as ex:
            print(ex)
    return info, save_file


# 根据经纬度计算两点之间距离
def geodistance(lonA, latA, lonB, latB):
    lonA, latA, lonB, latB = map(radians, [float(lonA), float(latA), float(lonB), float(latB)])  # 经纬度转换成弧度
    dlon = lonB - lonA
    dlat = latB - latA
    a = sin(dlat / 2) ** 2 + cos(latA) * cos(latB) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance, 3)
    return distance


# 返回B点相较于A点的方位角
def getDegree(lonA, latA, lonB, latB):
    """
    Args:
        point p1(latA, lonA)
        point p2(latB, lonB)
    Returns:
        bearing between the two GPS points,
        default: the basis of heading direction is north
    """
    radLatA = radians(latA)
    radLonA = radians(lonA)
    radLatB = radians(latB)
    radLonB = radians(lonB)
    dLon = radLonB - radLonA
    y = sin(dLon) * cos(radLatB)
    x = cos(radLatA) * sin(radLatB) - sin(radLatA) * cos(radLatB) * cos(dLon)
    brng = degrees(atan2(y, x))
    brng = (brng + 360) % 360
    return brng


def get_angle(degree_A, degree_B):
    bigger = max(degree_A, degree_B)
    smaller = min(degree_A, degree_B)
    if bigger - smaller > 180:
        return smaller+360-bigger
    else:
        return bigger-smaller


# 更改css和js文件地址到本地
def boost_html(file_name):
    file = open(os.path.dirname(os.getcwd()) + '/dataset/' + file_name, 'rb')
    html = file.read()
    bs = BeautifulSoup(html, "html.parser")
    for item in bs.head.find_all('script'):
        print(item)


def get_cross_info(cross_info_df):
    cross_info_df = cross_info_df.fillna(-1)
    cross_info_raw = cross_info_df.values.tolist()
    cross_info = []
    for raw_single_cross_info in cross_info_raw:
        i = 0
        single_cross_info = []
        for ele in raw_single_cross_info:
            if i == 6 or i == 7 or i == 11 or i == 12 or i == 16 or i == 17 or i == 21 or i == 22 or i == 26 or i == 27:
                if ele != -1:
                    single_cross_info.append(int(ele))
            elif i == 4 or i == 9 or i == 14 or i == 19 or i == 24 or i == 29:
                if ele != -1:
                    single_cross_info.append(round(ele, 3))
            else:
                if ele != -1:
                    single_cross_info.append(ele)
            i += 1
        cross_info.append(single_cross_info)
    return cross_info


def get_details(cross_info):
    next_state_list = []
    distance_list = []
    action_list = []
    tel_list = []
    for single_cross_info in cross_info:
        next_state_list_ = []
        distance_list_ = []
        action_list_ = []
        try:
            next_state_list_.append(single_cross_info[1])
            next_state_list_.append(single_cross_info[6])
            next_state_list_.append(single_cross_info[11])
            next_state_list_.append(single_cross_info[16])
            next_state_list_.append(single_cross_info[21])
            # next_state_list_.append(single_cross_info[26])
        except:
            next_state_list.append(next_state_list_)
        else:
            next_state_list.append(next_state_list_)
        try:
            distance_list_.append(single_cross_info[4])
            distance_list_.append(single_cross_info[9])
            distance_list_.append(single_cross_info[14])
            distance_list_.append(single_cross_info[19])
            distance_list_.append(single_cross_info[24])
            # distance_list_.append(single_cross_info[29])
        except:
            distance_list.append(distance_list_)
        else:
            distance_list.append(distance_list_)
        try:
            action_list_.append(single_cross_info[5])
            action_list_.append(single_cross_info[10])
            action_list_.append(single_cross_info[15])
            action_list_.append(single_cross_info[20])
            action_list_.append(single_cross_info[25])
            # action_list_.append(single_cross_info[30])
        except:
            action_list.append(action_list_)
        else:
            action_list.append(action_list_)
        # tel_list.append(single_cross_info[31])

    return next_state_list, distance_list, action_list, tel_list
