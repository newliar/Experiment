import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt

import configuration
from RL_brain import QLearningTable
from cross_2th_env import Cross_2th


class UpdateRealtime:

    def __init__(self, actions, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list,
                 action_list, tel_list, df_tel):
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
        self.tel_list = tel_list
        self.df_tel = df_tel

    def update_realtime(self):
        error_point = [155, 199, 306, 457, 116, 461, 626, 750, 240, 189, 485, 380, 116]
        time_start = time.time()
        # TODO Start_Point & End_Point 待输入
        for i in range(166, 288):

            # 随机种子，保证和第一次训练是相同的
            np.random.seed(i)
            start_point = np.random.randint(0, 800)
            if start_point in error_point:
                continue
            end_point = np.random.randint(801, 1725)

            # 读取已经存在本地的Q表
            df_q_table = pd.read_csv(os.getcwd() + '/table/' + configuration.CITY + '_' + str(start_point) + '_' + str(
                end_point) + '_' + 'q_table.csv', encoding="utf-8")
            df_q_table = df_q_table.set_index(['Unnamed: 0'])
            df_q_table = df_q_table[['1', '2', '3', '4']].astype(np.float64)
            RL = QLearningTable(self.actions)

            # 贪心策略设置为1
            RL.epsilon = 1
            # 更换Q表
            RL.q_table = df_q_table

            env = Cross_2th(self.next_state_list, self.action_list, self.distance_list, start_point, end_point, self.cross_info, self.tel_list, self.df_tel)
            # update block
            for episode in range(100):
                one_episode_start_time = time.time()
                plt.ion()
                observation = env.start_point
                while True:
                    index = RL.choose_action(observation, env, 2)
                    observation_, reward, done = env.step_2th(observation, index)

                    # plt.clf()
                    # plt.scatter(self.x[start_point], self.y[start_point], marker='o', s=100, label='start_point',
                    #             c='yellow')
                    # plt.scatter(self.x[end_point], self.y[end_point], marker='^', s=100, label='end_point', c='yellow')
                    # plt.scatter(self.x, self.y, s=15, alpha=0.3, c='green')
                    # if observation_ == 'end_point':
                    #     plt.scatter(self.x[end_point], self.y[end_point], s=15, c='red')
                    # elif observation_ == 'terminal':
                    #     plt.scatter(self.x[observation], self.y[observation], s=15, c='yellow')
                    # else:
                    #     plt.scatter(self.x[observation_], self.y[observation_], s=15, c='red')
                    # plt.pause(0.01)
                    # plt.ioff()

                    q_table = RL.learn(observation, index, reward, observation_, 2)

                    observation = observation_
                    current_time = time.time()
                    if current_time - one_episode_start_time > 180:
                        break
                    if done:
                        break
                one_episode_end_time = time.time()
                print('==========================================')
                print(episode + 1, "th episode is completed, time cost:", one_episode_end_time - one_episode_start_time)
                print('==========================================')
                print(q_table)
            q_table.to_csv(os.getcwd() + '/table_realtime/' + configuration.CITY + '_' + str(start_point) + '_' + str(
                end_point) + '_realtime_q_table.csv', encoding="utf-8")
        time_end = time.time()
        print('totally completely, time cost:', time_end - time_start)
