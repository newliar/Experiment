import pandas as pd
import os
import configuration
import tools
from update_static import UpdateStatic

ACTIONS = ['1', '2', '3', '4']


if __name__ == "__main__":
    df_re = pd.read_csv(
        os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv',
        encoding='utf-8')
    df_co = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_node&tel.csv',
                        encoding='utf-8')
    x = df_co['lon'].round(decimals=6).tolist()
    y = df_co['lat'].round(decimals=6).tolist()
    cross_relation = tools.get_cross_info(df_re)
    cross_info = df_co.values.tolist()
    next_state_list, distance_list, action_list = tools.get_details(cross_relation)

    us = UpdateStatic(ACTIONS, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list, action_list)
    UpdateStatic.update(us)
