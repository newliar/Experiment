import os
import numpy as np
import pandas as pd
import json

file_path = os.path.dirname(os.getcwd()) + "/dataset/node.json"
file = open(file_path, 'r', encoding='utf-8')
coordinate = []
for line in file.readlines():
    dic = json.loads(line)
    _coordinate = []
    _coordinate.append(dic["id"])
    _coordinate.append(np.float64(dic["lat"]))
    _coordinate.append(np.float64(dic["lon"]))
    coordinate.append(_coordinate)
columns = ['ref', 'lon', 'lat']
save_file = pd.DataFrame(columns=columns, data=coordinate)
save_file.to_csv('id_coordinate.csv', index=False, encoding="utf-8")