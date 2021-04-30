import pandas as pd
import numpy as np
import os
import random

import tools
import configuration

tel_station_file_path = os.path.dirname(os.getcwd()) + '/dataset/' + configuration.CITY + '_tel_station.csv'
df = pd.read_csv(tel_station_file_path, encoding='utf-8')
# df = df.append([1,2,3,4])
print(df)
df.loc['new_row']=1
print(df[df['index'].isin([787])].empty)
# print(df.loc[df['index'] == 787])
# print(random.choice(list(map(int, df['delay'].loc[df.loc[df['index'] == 790].index[0]][1:-1].split(',')))))
# print(random.choice(list(map(int, df['delay'].loc[790][1:-2].split(',')))))
# tel = []
# for index, row in df.iterrows():
#     if 117.2111 <= row['扇区经度'] <= 117.3731 and 31.6906 <= row['扇区纬度'] <= 31.8079:
#         np.random.seed(index)
#         delay = np.random.randint(3, 20, size=10)
#         tel.append([index, row['扇区经度'], row['扇区纬度'], delay])
# df = pd.DataFrame(tel, columns=['index', 'lon', 'lat', 'delay'])
# df.set_index('index', inplace=True)
# df.to_csv(os.path.dirname(os.getcwd()) + '/dataset/' + configuration.CITY + '_tel_station.csv', encoding='utf-8')
