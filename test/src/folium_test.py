import pandas as pd
import numpy as np
import os
import folium
from folium import plugins
import webbrowser

# full = pd.read_csv("F:/Experiment/test/dataset/tel_location.csv")
# full = full.dropna()
#
# schools_map = folium.Map(location=[full['lat'].mean(), full['lon'].mean()], zoom_start=10)
# marker_cluster = plugins.MarkerCluster().add_to(schools_map)
#
# for name,row in full.iterrows():
#      folium.Marker(
#         [row["lat"], row["lon"]],
#         # popup="{0}:{1}".format(row["cities"], row["GDP"])
#      ).add_to(marker_cluster)


