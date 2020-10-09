import os
import numpy as np
import pandas as pd
import json
import configuration

file_path = os.path.dirname(os.getcwd()) + "/dataset/"+configuration.CITY+"_node.json"
file = open(file_path, 'r', encoding='utf-8')
coordinate = []
for line in file.readlines():
    dic = json.loads(line)
    _coordinate = []
    if dic["id"] in coordinate:
        continue
    else:
        _coordinate.append(dic["id"])
        _coordinate.append(np.float64(dic["lon"]))
        _coordinate.append(np.float64(dic["lat"]))
        coordinate.append(_coordinate)
columns = ['ref', 'lon', 'lat']
save_file = pd.DataFrame(columns=columns, data=coordinate)
# save_file.set_index(['ref'], inplace=True)
save_file.to_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_id_coordinate.csv', index=False, encoding="utf-8")

