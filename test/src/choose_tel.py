import pandas as pd
import numpy as np
import os
import configuration
import tools
import math
import random


def get_queue_time() -> int:
    return random.randint(0, 10)


def get_process_time(task_size: int, tel_num: int) -> int:
    np.random.seed(tel_num)
    # process_speed = np.random.randint(10, 25)
    process_speed = configuration.CPU_CLOCK
    process_time = task_size/process_speed
    return process_time


class Choose:
    def __init__(self):
        self.node_info_file = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY +
                                          '_node&tel.csv', encoding='utf-8')
        self.tel_station_file = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY +
                                            '_tel_station.csv', encoding='utf-8')

    def get_transfer_time(self, task_size: int, state: int, tel_num: int) -> int:
        state_lon = self.node_info_file.loc[state].loc['lon']
        state_lat = self.node_info_file.loc[state].loc['lat']
        tel_lon = self.tel_station_file.loc[tel_num].loc['lon']
        tel_lat = self.tel_station_file.loc[tel_num].loc['lat']
        # tel_index = self.tel_station_file.loc[tel_num].loc['index']
        distance = tools.geodistance(state_lon, state_lat, tel_lon, tel_lat)
        x_1 = math.log(distance, 10)
        transfer_speed = 20 * math.log(1 + (0.5 * (127 + 30 * math.log(distance, 10))) / 0.002, 2)
        transfer_time = task_size/transfer_speed*1000
        return transfer_time
