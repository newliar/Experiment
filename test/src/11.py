import pandas as pd
import numpy as np


x = ['1','2','3']
y = ['4','5','6']

data = pd.DataFrame({'x':x,'y':y})
print(data.info())

data = data[['x','y']].astype(np.int32)
print(data.info())