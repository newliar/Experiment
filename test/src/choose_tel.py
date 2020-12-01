import pandas as pd
import os
import configuration
import tools
import math


class Choose:
    def __init__(self):
        self.node_info_file = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY +
                                          '_node&tel.csv', encoding='utf-8')
        self.tel_station_file = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY +
                                            '_tel_station.csv', encoding='utf-8')

    def choose_tel_station(self, task_size, state, tel_num):
        state_lon = self.node_info_file.loc[state].loc['lon']
        state_lat = self.node_info_file.loc[state].loc['lat']
        tel_lon = self.tel_station_file.loc[tel_num].loc['lon']
        tel_lat = self.tel_station_file.loc[tel_num].loc['lat']
        # tel_index = self.tel_station_file.loc[tel_num].loc['index']
        distance = tools.geodistance(state_lon, state_lat, tel_lon, tel_lat)
        x_1 = math.log(distance, 10)
        transfer_speed = 20*math.log(1+(0.5*(127+30*math.log(distance, 10)))/0.002, 2)
        print(distance, transfer_speed)



