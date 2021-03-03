import folium
import numpy as np
import pandas as pd
import os
import configuration
from folium.plugins import HeatMap


tel_file = pd.read_excel(os.path.dirname(os.getcwd())+'\\dataset\\'+configuration.CITY+'_tel_station.xls')
lat = tel_file['扇区纬度']
lon = tel_file['扇区经度']
data = [[lat[i], lon[i], 1] for i in range(8707)]
map_osm = folium.Map(location=[31.75, 117.32], zoom_start=5)
HeatMap(data).add_to(map_osm)
file_path = os.path.dirname(os.getcwd())+'\\dataset\\人口.html'
map_osm.save(file_path)     # 保存为html文件
print(lat, lon)
