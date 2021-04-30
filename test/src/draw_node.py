import folium
import pandas as pd
import os
import numpy as np

m = folium.Map([31.75, 117.29], zoom_start=13)
file_path = os.path.dirname(os.getcwd()) + '//dataset//HF_BH_public_node_info.csv'
df = pd.read_csv(file_path, encoding='utf-8')
cross_list = np.array(df).tolist()
for cross in cross_list:
    coordinate = [cross[2], cross[1]]
    folium.Marker(
        coordinate,
        color='#123456',
        radius=8
    ).add_to(m)
m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'HF_BH_public_node.html'))
