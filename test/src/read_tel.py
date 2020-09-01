import pandas as pd
import numpy as np

io = r'F:\Experiment\test\dataset\data_6.1~6.30_.xlsx'
data = pd.read_excel(io, sheet_name=1, usecols=[4])
data = data.dropna(axis=0, how='any')
location = data.values
s = set()
for line in location:
    s.add(line[0])
li = list(s)
location_ = []
for i in range(len(li)):
    location_.append(li[i].split('/'))
    temp = location_[i][0]
    location_[i][0] = location_[i][1]
    location_[i][1] = temp
location_np = np.array(location_)
df = pd.DataFrame(location_np)
df.columns = ['lon', 'lat']
df.to_csv('tel_location.csv', index=False)

# np.savetxt('F:\\Experiment\\test\\dataset\\tel_location.csv', location_np, delimiter=',')

