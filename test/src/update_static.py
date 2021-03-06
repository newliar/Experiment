import numpy as np
import os
import time
import matplotlib.pyplot as plt

import configuration
from RL_brain import QLearningTable
import tools
from cross_env import Cross


class UpdateStatic:

    def __init__(self, actions, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list, action_list):
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

    def update(self):
        # TODO Start_Point & End_Point 待输入
        for i in range(166, 288):
            np.random.seed(i)
            start_point = np.random.randint(0, 800)
            end_point = np.random.randint(801, 1725)
            RL = QLearningTable(self.actions)
            env = Cross(self.next_state_list, self.action_list, self.distance_list, start_point, end_point, self.cross_info)
            # update block
            time_start = time.time()
            for episode in range(100):
                # import SA
                T = 1000
                epsilon, T = tools.SA(T, episode, 100, 0.95)
                RL.epsilon = epsilon
                if epsilon > 1:
                    print("yes")
                print(epsilon)
                episode_start_time = time.time()
                plt.ion()
                observation = env.start_point
                prior_state = observation
                while True:
                    index = RL.choose_action(observation, env, 1)

                    observation_, reward, done = env.step(observation, index, prior_state)

                    # print("observation_:", observation_, "observation:", observation, "prior_state:", prior_state)

                    # 画图可视化
                    # plt.clf()
                    # plt.scatter(self.x[start_point], self.y[start_point], marker='o', s=100, label='start_point', c='yellow')
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

                    q_table = RL.learn(observation, index, reward, observation_, 1)
                    # print(q_table.loc[observation_])

                    prior_state = observation
                    observation = observation_
                    current_time = time.time()
                    if current_time - episode_start_time > 60:
                        break
                    if done:
                        break
                episode_end_time = time.time()
                print('==========================================')
                print(episode + 1, "th episode is completed, time cost:", episode_end_time - episode_start_time)
                print('==========================================')
                print(q_table)

            time_end = time.time()
            print('totally completely, time cost:', time_end - time_start)
            if 1 - bool(os.path.exists(os.getcwd() + '/table_' + str(configuration.Omega))):
                os.makedirs(os.getcwd() + '/table_' + str(configuration.Omega))
            q_table.to_csv(os.getcwd() + '/table_' + str(configuration.Omega) + '/' + configuration.CITY + '_' +
                           str(start_point) + '_' + str(end_point) + '_' + 'q_table.csv', encoding="utf-8")
