import matplotlib.pyplot as plt
import os
import pandas as pd

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
#
# x = list(range(len(num_list)))
# total_width, n = 0.8, 2
# width = total_width / n
# plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc='b')
# plt.xlabel('task size(mb)')
# plt.ylabel('time cost(s)')
# for i in range(len(x)):
#     x[i] += width
# plt.legend(['RLVPP'])
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


x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc='b')
plt.xlabel('cpu clock(Ghz)')
plt.ylabel('time cost(s)')
for i in range(len(x)):
    x[i] += width
plt.legend(['RLVPP'])
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