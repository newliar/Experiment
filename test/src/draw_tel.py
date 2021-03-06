import matplotlib.pyplot as plt
import folium
import pandas as pd
import os
import numpy as np

file_path = os.path.dirname(os.getcwd()) + '//dataset//基站信息.csv'
df = pd.read_csv(file_path)

map = folium.Map([31.75, 117.29], zoom_start=13)
tel_list = np.array(df).tolist()
i = 0
for tel in tel_list:
        i += 1
        coordinate = [tel[3], tel[2]]
        # 地图显示
        # folium.Circle(
        #     coordinate,
        #     color='#123456',
        #     fill_color='#123456',
        #     radius=400,
        #     fill=True
        # ).add_to(map)
        folium.Marker(
            coordinate,
            color='#123456',
            radius=8
        ).add_to(map)
        print(i, tel[3], tel[2])
map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'HF_BH_tel_station_node.html'))

# location_ = df.values
# location_[:, [0, 1]] = location_[:, [1, 0]]
# location = location_.tolist()
#
# count = 0
# for coordinate in location:
#     # 选取指定经纬度范围内的坐标
#     if 121.4388 < coordinate[1] < 121.4846 and 31.2019 < coordinate[0] < 31.2411:
#         count += 1
#         # matplotlib显示
#         # plt.scatter(location[i, 0], location[i, 1], s=1, c='red')
#         print(coordinate)
#         # 地图显示
#         folium.Circle(
#             coordinate,
#             color='#123456',
#             fill_color='#123456',
#             radius=400,
#             fill=True
#         ).add_to(map)
        # folium.Marker(
        #     coordinate,
        #     color='#123456',
        #     radius=8
        # ).add_to(map)

# 地图显示
# map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'tel_station_node.html'))

# import folium
# latlon = [ (51.249443914705175, -0.13878830247011467), (51.249443914705175, -0.13878830247011467), (51.249768239976866, -2.8610415615063034)]
# mapit = folium.Map( location=[52.667989, -1.464582], zoom_start=6 )
# for coord in latlon:
#     folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )
#
# mapit.save( 'map.html')

# matplotlib显示
# plt.show()
# plt.savefig("all_node.svg", format="svg")