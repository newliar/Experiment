import pandas as pd
import os
import configuration
import tools
from update_static import UpdateStatic
from update_realtime import UpdateRealtime

ACTIONS = ['1', '2', '3', '4']

if __name__ == "__main__":
    # 读取文件  路口信息及连通关系和基站信息
    df_re = pd.read_csv(
        os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv',
        encoding='utf-8')
    df_co = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_node&tel.csv',
                        encoding='utf-8')

    df_tel = pd.read_csv(os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_tel_station.csv',
                         encoding='utf-8')
    # x,y为了方便画图
    x = df_co['lon'].round(decimals=6).tolist()
    y = df_co['lat'].round(decimals=6).tolist()

    cross_relation = tools.get_cross_info(df_re)
    cross_info = df_co.values.tolist()
    next_state_list, distance_list, action_list, tel_list = tools.get_details(cross_relation)

    # 第一次更新，基站延迟固定
    us = UpdateStatic(ACTIONS, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list,
                      action_list)
    UpdateStatic.update(us)

    # 第二次更新，基站延迟随机
    # ur = UpdateRealtime(ACTIONS, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list,
    #                     action_list, tel_list, df_tel)
    # UpdateRealtime.update_realtime(ur)
