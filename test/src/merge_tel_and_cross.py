import pandas as pd
import tools
import os
import numpy as np
from geopy.distance import geodesic
import configuration


cross_file_path = os.path.dirname(os.getcwd())+'/dataset/'+configuration.CITY+'_public_node_info_.csv'
tel_file_path = os.path.dirname(os.getcwd())+'/dataset/基站信息.csv'


df_cross = pd.read_csv(cross_file_path, encoding='utf-8')
df_cross.set_index('Unnamed: 0', inplace=True)

df_tel = pd.read_csv(tel_file_path, encoding='utf-8')

cross_list = np.array(df_cross).tolist()
tel_list = np.array(df_tel).tolist()

for cross in cross_list:

    for tel in tel_list:
        distance = tools.geodistance(lonA=cross[1], latA=cross[2], lonB=tel[2], latB=tel[3])
        print(distance)
        if distance < 400:
            print(cross, '------☆------', tel)


# tel = []
# i = 0
# for index_cr, row_cr in df_cross.iterrows():
#     i += 1
#     tel_ = []
#     j = 0
#     for index_tel, row_tel in df_tel.iterrows():
#         j += 1
#         distance = tools.geodistance(row_cr['lon'], row_cr['lat'], row_tel['lon'], row_tel['lat'])
#         if distance < 400:
#             print(i, j)
#             tel_.append(index_tel)
#     tel.append(tel_)
#
#
# tel_s = pd.Series(tel)
# df_cross['tel'] = tel_s

# df_re = pd.read_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_relation.csv', encoding='utf-8')
# df_re['tel'] = tel_s
# df_re.to_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_relation.csv', index=False, encoding="utf-8")

# df_cross.to_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_node&tel.csv', index=True, encoding="utf-8")
# cross_list = pd_cross.values.tolist()
# tel_list = pd_tel.values.tolist()
# cross_addition = []
# for cross in cross_list:
#     cross_addition_ = []
#     for tel in tel_list:
#         distance = tools.geodistance(cross[1], cross[2], tel[1], tel[2])
#         if distance < 300:
#             cross_addition_.append(int(tel[0]))
#     cross_addition.append(cross_addition_)
# ser = pd.Series(cross_addition, name='tel')
# result = pd.concat([pd_cross, ser], axis=1)
# return result


