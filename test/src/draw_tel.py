import matplotlib.pyplot as plt
import folium
import pandas as pd
import os

file_path = os.path.dirname(os.getcwd()) + "//dataset//tel_location.csv"
df = pd.read_csv(file_path)
location_ = df.values
location_[:, [0, 1]] = location_[:, [1, 0]]
location = location_.tolist()

map = folium.Map([31.05, 121.7], zoom_start=13)
count = 0
for coordinate in location:
    # 选取指定经纬度范围内的坐标
    if 121.6557 < coordinate[1] < 121.7889 and 30.9835 < coordinate[0] < 31.1009:
        count += 1
        # matplotlib显示
        # plt.scatter(location[i, 0], location[i, 1], s=1, c='red')
        print(coordinate)
        # 地图显示
        folium.Circle(
            coordinate,
            color='grey',
            radius=2000,
            fill=False
        ).add_to(map)

# 地图显示
map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'tel_station.html'))

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