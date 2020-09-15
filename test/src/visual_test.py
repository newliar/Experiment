import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random


df = pd.read_csv('public_node_info_.csv', encoding='utf-8')
x = df['lat'].round(decimals=6).tolist()
y = df['lon'].round(decimals=6).tolist()

plt.ion()
for i in range(500):
    rn = random.randint(0, 999)
    x_r = x[rn]
    y_r = y[rn]
    plt.clf()
    plt.scatter(x, y, s=15, alpha=0.5)
    plt.scatter(x_r, y_r, s=15, c='red')
    plt.pause(0.5)
    plt.ioff()