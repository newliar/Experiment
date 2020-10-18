import os
import pandas as pd
import numpy as np

import configuration


df = pd.read_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_relation.csv', encoding='utf-8')
distance_list = []
for index, row in df.iterrows():
    # print(row['distance_one'])
    if bool(1-np.isnan(row['distance_one'])):
        distance_list.append(row['distance_one'])
    if bool(1-np.isnan(row['distance_two'])):
        distance_list.append(row['distance_two'])
    if bool(1-np.isnan(row['distance_three'])):
        distance_list.append(row['distance_three'])
    if bool(1-np.isnan(row['distance_four'])):
        distance_list.append(row['distance_four'])
sum = 0
for ele in distance_list:
    sum += ele
average = sum/len(distance_list)



