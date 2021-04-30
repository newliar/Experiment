import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

# task_size
name_list = ['2', '4', '6', '8', '10']
file_1 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
print(file_1)
file_2 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
file_3 = os.getcwd() + '/time_cost/TASK_SIZE_300_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
file_4 = os.getcwd() + '/time_cost/TASK_SIZE_400_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
# file_5 = os.getcwd() + '/time_cost/TASK_SIZE_500_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
# df_1 = pd.read_csv(file_1, encoding='utf-8')
# df_2 = pd.read_csv(file_2, encoding='utf-8')
# df_3 = pd.read_csv(file_3, encoding='utf-8')
# df_4 = pd.read_csv(file_4, encoding='utf-8')
# df_5 = pd.read_csv(file_5, encoding='utf-8')
#
# transfer_time_1 = df_1['transfer']
# queue_time_1 = df_1['queue']
# process_time_1 = df_1['process']
# transfer_time_1_mean = transfer_time_1.mean()
# queue_time_1_mean = queue_time_1.mean()
# process_time_1_mean = process_time_1.mean()
#
# transfer_time_2 = df_2['transfer']
# queue_time_2 = df_2['queue']
# process_time_2 = df_2['process']
# transfer_time_2_mean = transfer_time_2.mean()
# queue_time_2_mean = queue_time_2.mean()
# process_time_2_mean = process_time_2.mean()
#
# transfer_time_3 = df_3['transfer']
# queue_time_3 = df_3['queue']
# process_time_3 = df_3['process']
# transfer_time_3_mean = transfer_time_3.mean()
# queue_time_3_mean = queue_time_3.mean()
# process_time_3_mean = process_time_3.mean()
#
# transfer_time_4 = df_4['transfer']
# queue_time_4 = df_4['queue']
# process_time_4 = df_4['process']
# transfer_time_4_mean = transfer_time_4.mean()
# queue_time_4_mean = queue_time_4.mean()
# process_time_4_mean = process_time_4.mean()
#
# transfer_time_5 = df_5['transfer']
# queue_time_5 = df_5['queue']
# process_time_5 = df_5['process']
# transfer_time_5_mean = transfer_time_5.mean()
# queue_time_5_mean = queue_time_5.mean()
# process_time_5_mean = process_time_5.mean()
#
# num_list = [(transfer_time_1_mean + queue_time_1_mean + process_time_1_mean) / 1000,
#             (transfer_time_2_mean + queue_time_2_mean + process_time_2_mean) / 1000,
#             (transfer_time_3_mean + queue_time_3_mean + process_time_3_mean) / 1000,
#             (transfer_time_4_mean + queue_time_4_mean + process_time_4_mean) / 1000,
#             (transfer_time_5_mean + queue_time_5_mean + process_time_5_mean) / 1000]
# print(num_list)
#
# dijkstra = [1824.984436 / 1000, 3151.591601 / 1000, 4473.910491 / 1000, 5790.181063 / 1000, 7111.579049 / 1000]
# random = [1899.450336 / 1000, 3187.471213 / 1000, 4516.197448 / 1000, 5865.98743 / 1000, 7165.158537 / 1000]
# rl_based = [1853.116187 / 1000, 3169.85901 / 1000, 4487.953964 / 1000, 5810.03919 / 1000, 7126.05258 / 1000]
#
# x = np.arange(5)
#
# width = 0.15
# plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc=(68/255, 1/255, 84/255))
# plt.bar(x + width, dijkstra, width=width, label='2', tick_label=name_list, fc=(49/255, 104/255, 142/255))
# plt.bar(x + 2 * width, random, width=width, label='3', tick_label=name_list, fc=(53/255, 183/255, 121/255))
# plt.bar(x + 3 * width, rl_based, width=width, label='4', tick_label=name_list, fc=(253/255, 231/255, 37/255))
# plt.xlabel('number of task')
# plt.ylabel('time cost(s)')
# plt.legend(['RLVPP', 'dijkstra', 'random', 'rl_based'])
# plt.xticks(x + 3 * width / 2, name_list)
# plt.savefig('./task_size.svg')
# plt.show()

# cpu clock
# name_list = ['10', '15', '20', '25', '30']
# file_1 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
# file_2 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.15_VEHICLE_POWER_0.5_time_cost.csv'
# file_3 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.2_VEHICLE_POWER_0.5_time_cost.csv'
# file_4 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.25_VEHICLE_POWER_0.5_time_cost.csv'
# file_5 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.3_VEHICLE_POWER_0.5_time_cost.csv'
# df_1 = pd.read_csv(file_1, encoding='utf-8')
# df_2 = pd.read_csv(file_2, encoding='utf-8')
# df_3 = pd.read_csv(file_3, encoding='utf-8')
# df_4 = pd.read_csv(file_4, encoding='utf-8')
# df_5 = pd.read_csv(file_5, encoding='utf-8')
#
# transfer_time_1 = df_1['transfer']
# queue_time_1 = df_1['queue']
# process_time_1 = df_1['process']
# transfer_time_1_mean = transfer_time_1.mean()
# queue_time_1_mean = queue_time_1.mean()
# process_time_1_mean = process_time_1.mean()
#
# transfer_time_2 = df_2['transfer']
# queue_time_2 = df_2['queue']
# process_time_2 = df_2['process']
# transfer_time_2_mean = transfer_time_2.mean()
# queue_time_2_mean = queue_time_2.mean()
# process_time_2_mean = process_time_2.mean()
#
# transfer_time_3 = df_3['transfer']
# queue_time_3 = df_3['queue']
# process_time_3 = df_3['process']
# transfer_time_3_mean = transfer_time_3.mean()
# queue_time_3_mean = queue_time_3.mean()
# process_time_3_mean = process_time_3.mean()
#
# transfer_time_4 = df_4['transfer']
# queue_time_4 = df_4['queue']
# process_time_4 = df_4['process']
# transfer_time_4_mean = transfer_time_4.mean()
# queue_time_4_mean = queue_time_4.mean()
# process_time_4_mean = process_time_4.mean()
#
# transfer_time_5 = df_5['transfer']
# queue_time_5 = df_5['queue']
# process_time_5 = df_5['process']
# transfer_time_5_mean = transfer_time_5.mean()
# queue_time_5_mean = queue_time_5.mean()
# process_time_5_mean = process_time_5.mean()
#
# num_list = [(transfer_time_1_mean + queue_time_1_mean + process_time_1_mean) / 1000,
#             (transfer_time_2_mean + queue_time_2_mean + process_time_2_mean) / 1000,
#             (transfer_time_3_mean + queue_time_3_mean + process_time_3_mean) / 1000,
#             (transfer_time_4_mean + queue_time_4_mean + process_time_4_mean) / 1000,
#             (transfer_time_5_mean + queue_time_5_mean + process_time_5_mean) / 1000]
#
#
# dijkstra = [1824.984436 / 1000, 1498.480967 / 1000, 1330.470572 / 1000, 1227.54973 / 1000, 1160.618838 / 1000]
# random = [1899.450336 / 1000, 1541.704681 / 1000, 1390.019189 / 1000, 1287.164508 / 1000, 1246.944968 / 1000]
# rl_based = [1853.116187 / 1000, 1515.377895 / 1000, 1350.561037 / 1000, 1250.891775 / 1000, 1182.954193 / 1000]
#
# x = np.arange(5)
# width = 0.15
# plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc=(68/255, 1/255, 84/255))
# plt.bar(x + width, dijkstra, width=width, label='2', tick_label=name_list, fc=(49/255, 104/255, 142/255))
# plt.bar(x + 2 * width, random, width=width, label='3', tick_label=name_list, fc=(53/255, 183/255, 121/255))
# plt.bar(x + 3 * width, rl_based, width=width, label='4', tick_label=name_list, fc=(253/255, 231/255, 37/255))
# plt.xlabel('cpu clock(Ghz)')
# plt.ylabel('time cost(s)')
# plt.legend(['RLVPP', 'dijkstra', 'random', 'rl_based'])
# plt.xticks(x + 3 * width / 2, name_list)
# plt.savefig('./cpu_clock.svg')
# plt.show()

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
