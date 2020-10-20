import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt

import configuration
import tools
from RL_brain import QLearningTable
from cross_2th_env import Cross_2th


class UpdateRealtime:

    def __init__(self, actions, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list,
                 action_list):
        self.actions = actions
        self.df_re = df_re
        self.df_co = df_co
        self.x = x
        self.y = y
        self.cross_relation = cross_relation
        self.cross_info = cross_info
        self.next_state_list = next_state_list
        self.distance_list = distance_list
        self.action_list = action_list

    def update_realtime(self):
        # TODO Start_Point & End_Point 待输入
        for i in range(166, 288):

            # 随机种子，保证和第一次训练是相同的
            np.random.seed(i)
            start_point = np.random.randint(0, 800)
            end_point = np.random.randint(801, 1725)

            # 读取已经存在本地的Q表
            df = pd.read_csv(os.getcwd() + '/table/' + configuration.CITY + '_' + str(start_point) + '_' + str(
                end_point) + '_' + 'q_table.csv', encoding="utf-8")
            RL = QLearningTable(self.actions)

            # 贪心策略设置为1
            RL.e_greedy = 1
            # 更换Q表
            RL.q_table = df

            env = Cross_2th(self.next_state_list, self.action_list, self.distance_list, start_point, end_point, self.cross_info)
            # update block
            time_start = time.time()
            for episode in range(100):
                episode_start_time = time.time()
                plt.ion()
                observation = env.start_point
                while True:
                    index = RL.choose_action(observation, env)
                    observation_, reward, done = env.step_2th(observation, index)

                    plt.clf()
                    plt.scatter(self.x[start_point], self.y[start_point], marker='o', s=100, label='start_point',
                                c='yellow')
                    plt.scatter(self.x[end_point], self.y[end_point], marker='^', s=100, label='end_point', c='yellow')
                    plt.scatter(self.x, self.y, s=15, alpha=0.3, c='green')
                    if observation_ == 'end_point':
                        plt.scatter(self.x[end_point], self.y[end_point], s=15, c='red')
                    elif observation_ == 'terminal':
                        plt.scatter(self.x[observation], self.y[observation], s=15, c='yellow')
                    else:
                        plt.scatter(self.x[observation_], self.y[observation_], s=15, c='red')
                    plt.pause(0.01)
                    plt.ioff()