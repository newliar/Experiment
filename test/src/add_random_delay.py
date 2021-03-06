import pandas as pd
import numpy as np
import os
import random

import configuration


df_tel = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_tel_station.csv', encoding='utf-8')
delay = []
for i in range(len(df_tel)):
    large = np.random.randint(10, 1000, 10).tolist()
    large.append(random.randint(0, 30))
    delay.append(large)
df_tel['delay'] = delay
df_tel.to_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_tel_station.csv', encoding='utf-8')