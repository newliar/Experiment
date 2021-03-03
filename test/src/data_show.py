import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

# task_size
# name_list = ['200', '300', '500']
# file_1 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.25_VEHICLE_POWER_0.5_time_cost.csv'
# file_2 = os.getcwd() + '/time_cost/TASK_SIZE_300_CPU_CLOCK_0.25_VEHICLE_POWER_0.5_time_cost.csv'
# file_3 = os.getcwd() + '/time_cost/TASK_SIZE_500_CPU_CLOCK_0.25_VEHICLE_POWER_0.5_time_cost.csv'
# df_1 = pd.read_csv(file_1, encoding='utf-8')
# df_2 = pd.read_csv(file_2, encoding='utf-8')
# df_3 = pd.read_csv(file_3, encoding='utf-8')
#
# transfer_time_1 = df_1['transfer']
# queue_time_1 = df_1['queue']
# process_time_1 = df_1['process']
# transfer_time_1_mean = transfer_time_1.mean()
# process_time_1_mean = process_time_1.mean()
#
# transfer_time_2 = df_2['transfer']
# queue_time_2 = df_2['queue']
# process_time_2 = df_2['process']
# transfer_time_2_mean = transfer_time_2.mean()
# process_time_2_mean = process_time_2.mean()
#
# transfer_time_3 = df_3['transfer']
# queue_time_3 = df_3['queue']
# process_time_3 = df_3['process']
# transfer_time_3_mean = transfer_time_3.mean()
# process_time_3_mean = process_time_3.mean()
#
# num_list = [(transfer_time_1_mean + process_time_1_mean)/1000,
#             (transfer_time_2_mean + process_time_2_mean)/1000,
#             (transfer_time_3_mean + process_time_3_mean)/1000]
#
# dijkstra = [1564.372837311976/1000, 2284.7912584829114/1000, 3725.929263980974/1000]
# random = [1724.6326755726093/1000, 2436.182682935416/1000, 3875.0482972592804/1000]
# rl_based = [1632.3589871076604/1000, 2347.451227006032/1000, 3787.4904429757707/1000]
#
# x = np.arange(3)
#
# width = 0.15
# plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc='r')
# plt.bar(x+width, dijkstra, width=width, label='2', tick_label=name_list, fc='y')
# plt.bar(x+2*width, random, width=width, label='3', tick_label=name_list, fc='g')
# plt.bar(x+3*width, rl_based, width=width, label='4', tick_label=name_list, fc='b')
# plt.xlabel('task size(mb)')
# plt.ylabel('time cost(s)')
# plt.legend(['RLVPP', 'dijkstra', 'random', 'rl_based'])
# plt.xticks(x + 3*width/2, name_list)
# plt.savefig('./task_size.svg')
# plt.show()

# cpu clock
name_list = ['25', '50', '100']
file_1 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.25_VEHICLE_POWER_0.5_time_cost.csv'
file_2 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.5_VEHICLE_POWER_0.5_time_cost.csv'
file_3 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_1_VEHICLE_POWER_0.5_time_cost.csv'
df_1 = pd.read_csv(file_1, encoding='utf-8')
df_2 = pd.read_csv(file_2, encoding='utf-8')
df_3 = pd.read_csv(file_3, encoding='utf-8')

transfer_time_1 = df_1['transfer']
queue_time_1 = df_1['queue']
process_time_1 = df_1['process']
transfer_time_1_mean = transfer_time_1.mean()
process_time_1_mean = process_time_1.mean()

transfer_time_2 = df_2['transfer']
queue_time_2 = df_2['queue']
process_time_2 = df_2['process']
transfer_time_2_mean = transfer_time_2.mean()
process_time_2_mean = process_time_2.mean()

transfer_time_3 = df_3['transfer']
queue_time_3 = df_3['queue']
process_time_3 = df_3['process']
transfer_time_3_mean = transfer_time_3.mean()
process_time_3_mean = process_time_3.mean()

num_list = [(transfer_time_1_mean + process_time_1_mean)/1000,
            (transfer_time_2_mean + process_time_2_mean)/1000,
            (transfer_time_3_mean + process_time_3_mean)/1000]

dijkstra = [1564.372837311976/1000, 1164.6985210592245/1000, 965.390127472302/1000]
random = [1724.6326755726093/1000, 1318.148095322494/1000, 1119.2114139795015/1000]
rl_based = [1632.3589871076604/1000, 1229.9247849461851/1000, 1029.5128332615072/1000]


x = np.arange(3)
width = 0.15
plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc='r')
plt.bar(x+width, dijkstra, width=width, label='2', tick_label=name_list, fc='y')
plt.bar(x+2*width, random, width=width, label='3', tick_label=name_list, fc='g')
plt.bar(x+3*width, rl_based, width=width, label='4', tick_label=name_list, fc='b')
plt.xlabel('cpu clock(Ghz)')
plt.ylabel('time cost(s)')
plt.legend(['RLVPP', 'dijkstra', 'random', 'rl_based'])
plt.xticks(x + 3*width/2, name_list)
plt.savefig('./cpu_clock.svg')
plt.show()


# vehicle power
# name_list = ['0.5', '1', '5']
# file_1 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.25_VEHICLE_POWER_0.5_time_cost.csv'
# file_2 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.25_VEHICLE_POWER_1_time_cost.csv'
# file_3 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.25_VEHICLE_POWER_5_time_cost.csv'
# df_1 = pd.read_csv(file_1, encoding='utf-8')
# df_2 = pd.read_csv(file_2, encoding='utf-8')
# df_3 = pd.read_csv(file_3, encoding='utf-8')
#
# transfer_time_1 = df_1['transfer']
# queue_time_1 = df_1['queue']
# process_time_1 = df_1['process']
# transfer_time_1_mean = transfer_time_1.mean()
# process_time_1_mean = process_time_1.mean()
#
# transfer_time_2 = df_2['transfer']
# queue_time_2 = df_2['queue']
# process_time_2 = df_2['process']
# transfer_time_2_mean = transfer_time_2.mean()
# process_time_2_mean = process_time_2.mean()

# transfer_time_3 = df_3['transfer']
# queue_time_3 = df_3['queue']
# process_time_3 = df_3['process']
# transfer_time_3_mean = transfer_time_3.mean()
# process_time_3_mean = process_time_3.mean()
#
# num_list = [(transfer_time_1_mean + process_time_1_mean)/1000,
#             (transfer_time_2_mean + process_time_2_mean)/1000,
#             (transfer_time_3_mean + process_time_3_mean)/1000]
#
#
# x = list(range(len(num_list)))
# total_width, n = 0.8, 2
# width = total_width / n
# plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc='b')
# plt.xlabel('cpu clock(w)')
# plt.ylabel('time cost(s)')
# for i in range(len(x)):
#     x[i] += width
# plt.legend(['RLVPP'])
# plt.show()