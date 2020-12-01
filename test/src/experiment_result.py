import numpy as np
import pandas as pd
import os
import configuration


if __name__ == '__main__':
    error_point = [750,  240,  189, 155, 199,  485, 306, 457,  380,  626,  116, 461]
    index = 0
    for i in range(166, 288):
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        if start_point in error_point:
            continue
        end_point = np.random.randint(801, 1725)
        first_table = pd.read_csv(os.getcwd() + "/table/" + configuration.CITY + '_' + str(start_point) + '_' +
                                  str(end_point) + '_q_table.csv', encoding='utf-8')
        second_table = pd.read_csv(os.getcwd() + "/table_realtime/" + configuration.CITY + '_' + str(start_point)
                                   + '_' + str(end_point) + '_realtime_q_table.csv', encoding='utf-8')
