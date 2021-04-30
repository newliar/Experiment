import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


def data_show():
    name_list = ['2', '4', '6', '8', '10']
    file_1 = os.getcwd() + '/time_cost/TASK_SIZE_100_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
    file_2 = os.getcwd() + '/time_cost/TASK_SIZE_200_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
    file_3 = os.getcwd() + '/time_cost/TASK_SIZE_300_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
    file_4 = os.getcwd() + '/time_cost/TASK_SIZE_400_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
    file_5 = os.getcwd() + '/time_cost/TASK_SIZE_500_CPU_CLOCK_0.1_VEHICLE_POWER_0.5_time_cost.csv'
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
