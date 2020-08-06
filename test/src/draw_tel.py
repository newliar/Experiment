import matplotlib.pyplot as plt
import folium
import pandas as pd
import os

file_path = os.path.dirname(os.getcwd()) + "//dataset//tel_location.csv"
df = pd.read_csv(file_path)
location = df.values
map = folium.Map([31.2329298, 121.4822705], zoom_start=6)
for i in range(3041):
    if 121.6 < location[i][0] < 121.78 and 30.9 < location[i][1] < 31.2:
        plt.scatter(location[i, 0], location[i, 1], s=1, c='red')
        # folium.Marker(
        #     location=location[i],
        #     fill_color='＃43d9de',
        #     radius=8
        # ).add_to(map)
        # print(location[i])

#
#
# for coordinate in location:
#     folium.Marker(
#         location=coordinate,
#         fill_color='＃43d9de',
#         radius=8
#     ).add_to(map)
#
# map.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'tel_station.html'))

# for i in range(3041):
#     plt.scatter(location[i, 0], location[i, 1], s=1, c='red')
plt.show()
# plt.savefig("all_node.svg", format="svg")