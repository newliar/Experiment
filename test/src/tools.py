import matplotlib.pyplot as plt
import folium
import os
import pandas as pd
from math import radians, cos, sin, asin, sqrt, atan2, degrees
from bs4 import BeautifulSoup


# 画两条线段
def draw_line():
    plt.scatter(121.771594 * 1000000, 31.055035 * 1000000, color='red')
    plt.scatter(121.7716 * 1000000, 31.055103 * 1000000, color='red')
    # plt.scatter(121.737941*1000000, 31.042536*1000000, color='blue')
    # plt.scatter(121.737857*1000000, 31.042544*1000000, color='blue')


# draw_line()
# plt.show()
# plt.savefig("line.svg", format="svg")

def draw_node(map, all_location):
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
            ).add_to(map)
    return map


def write_cross_to_file(cross_coordinate):
    index = 0
    info = []
    for ele in cross_coordinate:
        info.append([ele[0][0], ele[0][1],
                     ele[1][0], ele[1][1],
                     round(ele[2][0], 7), round(ele[2][1], 7)])
        print(str(index)+ele[0][1])
        index += 1
    columns = ['way_one_id', 'way_one_name', 'way_two_id', "way_two_name", "lon", "lat"]
    save_file = pd.DataFrame(columns=columns, data=info)
    try:
        save_file.to_csv('cross_info.csv', index=True, encoding="gb2312")
    except:
        os.remove('cross_info.csv')
        try:
            save_file.to_csv('cross_info.csv', index=True, encoding="gb2312")
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


# 更改css和js文件地址到本地
def boost_html(file_name):
    file = open(os.path.dirname(os.getcwd()) + '/dataset/' + file_name, 'rb')
    html = file.read()
    bs = BeautifulSoup(html, "html.parser")
    for item in bs.head.find_all('script'):
        print(item)
