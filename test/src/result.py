import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

# dijkstra = [5412.214435 *0.8 + 1741.5870569199803 *0.5, 5412.214435 *0.8 + 2980.456300456336 *0.5,
#             5412.214435 *0.8 + 4225.245760769263 *0.5, 5412.214435 *0.8 + 5456.991630130356 *0.5,
#             5412.214435 *0.8 + 6696.182551329113 *0.5]
# random = [5412.214435 *0.8 + 1777.2504780096647 *0.5, 5412.214435 *0.8 + 3023.6490202319465 *0.5,
#           5412.214435 *0.8 + 4251.482652840129 *0.5, 5412.214435 *0.8 + 5465.216725821892 *0.5,
#           5412.214435 *0.8 + 6772.083728115029 *0.5]
# rl_based = [5412.214435 *0.8 + 1759.999700223032 *0.5, 5412.214435 *0.8 + 2993.215955067971 *0.5,
#             5412.214435 *0.8 + 4227.909660893313 *0.5, 5412.214435 *0.8 + 5469.5771762424665 *0.5,
#             5412.214435 *0.8 + 6703.970685989072 *0.5]
# name_list = ['2', '4', '6', '8', '10']
# file_1 = os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.1_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
# file_2 = os.getcwd() + '/table_realtime_Ω_0.5_ts_200_cc_0.1_vp_666/time_cost/TASK_SIZE_200_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
# file_3 = os.getcwd() + '/table_realtime_Ω_0.5_ts_300_cc_0.1_vp_666/time_cost/TASK_SIZE_300_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
# file_4 = os.getcwd() + '/table_realtime_Ω_0.5_ts_400_cc_0.1_vp_666/time_cost/TASK_SIZE_400_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
# file_5 = os.getcwd() + '/table_realtime_Ω_0.5_ts_500_cc_0.1_vp_666/time_cost/TASK_SIZE_500_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
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
# num_list = [5412.214435 *0.8+(transfer_time_1_mean + queue_time_1_mean + process_time_1_mean)*0.5,
#             5412.214435 *0.8+(transfer_time_2_mean + queue_time_2_mean + process_time_2_mean)*0.5,
#             5412.214435 *0.8+(transfer_time_3_mean + queue_time_3_mean + process_time_3_mean)*0.5,
#             5412.214435 *0.8+(transfer_time_4_mean + queue_time_4_mean + process_time_4_mean)*0.5,
#             5412.214435 *0.8+(transfer_time_5_mean + queue_time_5_mean + process_time_5_mean)*0.5]
#
# x = np.arange(5)
#
#
# # plt.plot(name_list, num_list, color='red', linewidth=2.0, linestyle='--')
# # plt.plot(name_list, dijkstra, color='blue', linewidth=2.0, linestyle='-')
# # plt.plot(name_list, random, color='green', linewidth=2.0, linestyle=':')
# # plt.plot(name_list, rl_based, color='yellow', linewidth=2.0, linestyle='-.')
# width = 0.15
# plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc=(68/255, 1/255, 84/255))
# plt.bar(x + width, dijkstra, width=width, label='2', tick_label=name_list, fc=(49/255, 104/255, 142/255))
# plt.bar(x + 2 * width, random, width=width, label='3', tick_label=name_list, fc=(53/255, 183/255, 121/255))
# plt.bar(x + 3 * width, rl_based, width=width, label='4', tick_label=name_list, fc=(253/255, 231/255, 37/255))
# plt.xlabel('number of task(ω=0.8)')
# plt.ylabel('total cost')
# plt.legend(['RLVPP', 'dijkstra', 'random', 'rl_based'])
# plt.xticks(x + 3 * width / 2, name_list)
# plt.savefig('./0.8_task_size.svg')
# plt.show()

# cpu clock
name_list = ['10', '15', '20', '25', '30']
file_1 = os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.1_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.1_VEHICLE_POWER_666_time_cost.csv'
file_2 = os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.15_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.15_VEHICLE_POWER_666_time_cost.csv'
file_3 = os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.2_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.2_VEHICLE_POWER_666_time_cost.csv'
file_4 = os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.25_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.25_VEHICLE_POWER_666_time_cost.csv'
file_5 = os.getcwd() + '/table_realtime_Ω_0.5_ts_100_cc_0.3_vp_666/time_cost/TASK_SIZE_100_CPU_CLOCK_0.3_VEHICLE_POWER_666_time_cost.csv'
df_1 = pd.read_csv(file_1, encoding='utf-8')
df_2 = pd.read_csv(file_2, encoding='utf-8')
df_3 = pd.read_csv(file_3, encoding='utf-8')
df_4 = pd.read_csv(file_4, encoding='utf-8')
df_5 = pd.read_csv(file_5, encoding='utf-8')

transfer_time_1 = df_1['transfer']
queue_time_1 = df_1['queue']
process_time_1 = df_1['process']
transfer_time_1_mean = transfer_time_1.mean()
queue_time_1_mean = queue_time_1.mean()
process_time_1_mean = process_time_1.mean()

transfer_time_2 = df_2['transfer']
queue_time_2 = df_2['queue']
process_time_2 = df_2['process']
transfer_time_2_mean = transfer_time_2.mean()
queue_time_2_mean = queue_time_2.mean()
process_time_2_mean = process_time_2.mean()

transfer_time_3 = df_3['transfer']
queue_time_3 = df_3['queue']
process_time_3 = df_3['process']
transfer_time_3_mean = transfer_time_3.mean()
queue_time_3_mean = queue_time_3.mean()
process_time_3_mean = process_time_3.mean()

transfer_time_4 = df_4['transfer']
queue_time_4 = df_4['queue']
process_time_4 = df_4['process']
transfer_time_4_mean = transfer_time_4.mean()
queue_time_4_mean = queue_time_4.mean()
process_time_4_mean = process_time_4.mean()

transfer_time_5 = df_5['transfer']
queue_time_5 = df_5['queue']
process_time_5 = df_5['process']
transfer_time_5_mean = transfer_time_5.mean()
queue_time_5_mean = queue_time_5.mean()
process_time_5_mean = process_time_5.mean()

num_list = [5412.214435 * 0.5+(transfer_time_1_mean + queue_time_1_mean + process_time_1_mean)*0.5,
            5412.214435 * 0.5+(transfer_time_2_mean + queue_time_2_mean + process_time_2_mean)*0.5,
            5412.214435 * 0.5+(transfer_time_3_mean + queue_time_3_mean + process_time_3_mean)*0.5,
            5412.214435 * 0.5+(transfer_time_4_mean + queue_time_4_mean + process_time_4_mean)*0.5,
            5412.214435 * 0.5+(transfer_time_5_mean + queue_time_5_mean + process_time_5_mean)*0.5]
dijkstra = [5412.214435 * 0.5+1741.5870569199803*0.5, 5412.214435 * 0.5+1406.1345906931144*0.5, 5412.214435 * 0.5+1241.2415338285275*0.5, 5412.214435 * 0.5+1143.751147400622*0.5, 5412.214435 * 0.5+1075.3975344568723*0.5]
random = [5412.214435 * 0.5+1777.2504780096647*0.5, 5412.214435 * 0.5+1456.816093843523*0.5, 5412.214435 * 0.5+1290.565492236635*0.5, 5412.214435 * 0.5+1176.2575408480675*0.5, 5412.214435 * 0.5+1146.400927263395*0.5]
rl_based = [5412.214435 * 0.5+1759.999700223032*0.5, 5412.214435 * 0.5+1429.1376834163493*0.5, 5412.214435 * 0.5+1261.2940419597933*0.5, 5412.214435 * 0.5+1164.7715489626119*0.5, 5412.214435 * 0.5+1089.1445461614123*0.5]

x = np.arange(5)
width = 0.15
plt.bar(x, num_list, width=width, label='1', tick_label=name_list, fc=(68/255, 1/255, 84/255))
plt.bar(x + width, dijkstra, width=width, label='2', tick_label=name_list, fc=(49/255, 104/255, 142/255))
plt.bar(x + 2 * width, random, width=width, label='3', tick_label=name_list, fc=(53/255, 183/255, 121/255))
plt.bar(x + 3 * width, rl_based, width=width, label='4', tick_label=name_list, fc=(253/255, 231/255, 37/255))
plt.xlabel('cpu clock(Ghz)(ω=0.5)')
plt.ylabel('total cost')
plt.legend(['RLVPP', 'dijkstra', 'random', 'rl_based'])
plt.xticks(x + 3 * width / 2, name_list)
plt.savefig('./0.5_cpu_clock.svg')
plt.show()