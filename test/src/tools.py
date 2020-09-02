import matplotlib.pyplot as plt
import folium
import os
from bs4 import BeautifulSoup


# 画两条线段
def draw_line():
    plt.scatter(121.771594*1000000, 31.055035*1000000, color='red')
    plt.scatter(121.7716*1000000, 31.055103*1000000, color='red')
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


# 更改css和js文件地址到本地
def boost_html(file_name):
    file = open(os.path.dirname(os.getcwd()) + '/dataset/' + file_name, 'rb')
    html = file.read()
    bs = BeautifulSoup(html, "html.parser")
    for item in bs.head.find_all('script'):
        print(item)

