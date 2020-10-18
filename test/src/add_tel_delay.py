import pandas as pd
import numpy as np
import os

import tools
import configuration

tel_station_file_path = os.path.dirname(os.getcwd()) + '/dataset/' + configuration.CITY + '_tel_station.xls'
df = pd.read_excel(tel_station_file_path, encoding='utf-8')
tel = []
for index, row in df.iterrows():
    if 117.2111 <= row['扇区经度'] <= 117.3731 and 31.6906 <= row['扇区纬度'] <= 31.8079:
        np.random.seed(index)
        delay = np.random.randint(3, 20, size=10)
        tel.append([index, row['扇区经度'], row['扇区纬度'], delay])
df = pd.DataFrame(tel, columns=['index', 'lon', 'lat', 'delay'])
df.set_index('index', inplace=True)
df.to_csv(os.path.dirname(os.getcwd()) + '/dataset/' + configuration.CITY + '_tel_station.csv', encoding='utf-8')
