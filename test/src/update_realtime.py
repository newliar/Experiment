import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt

import configuration
from RL_brain import QLearningTable
from cross_2th_env import Cross_2th
import tools


class UpdateRealtime:

    def __init__(self, actions, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list,
                 action_list, tel_list, df_tel, omega):
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
        self.omega = omega

    def update_realtime(self):
        # error_point = [256, 512, 768, 3, 5, 778, 138, 779, 655, 786, 789, 793, 155, 34, 675, 420, 293, 424, 169, 428, 301,
        #                173, 431, 49, 306, 182, 439, 701, 189, 65, 322, 199, 456, 457, 461, 725, 599, 345, 732, 734, 351,
        #                98, 485, 742, 104, 490, 620, 750, 240, 753, 626, 116, 380]
        # error_point = [750, 240, 189, 155, 199, 485, 306, 457, 380, 626, 116, 461]
        error_point = [512, 5, 138, 779, 280, 155, 34, 675, 420, 424, 301, 430, 306, 439, 701, 189, 317, 63, 322, 199,
                       457, 461, 589, 725, 215, 599, 345, 732, 351, 609, 485, 620, 240, 626, 380]
        # time_start = time.time()
        error_list = []
        # TODO Start_Point & End_Point 待输入
        # delay_col = {'s_e', 'start_point', 'end_point', 'transfer', 'queue', 'process'}
        delay_df = pd.DataFrame(columns=('s_e', 'start_point', 'end_point', 'transfer', 'queue', 'process'))
        # delay_df = delay_df.append({'s_e': 'TASK_SIZE:'+str(configuration.TASK_SIZE),山西053乡道
        #                             'start_point:': 'CPU_CLOCK'+str(configuration.CPU_CLOCK),
        #                             'end_point:': 'VEHICLE_POWER'+str(configuration.VEHICLE_POWER),
        #                             'transfer': 000,
        #                             'queue': 000,
        #                             'process': 000},
        #                            ignore_index=True)
        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cost_list = []
        # for z in range(10):
        time_start = time.time()
        count = 0
        e_count = 0
        for i in range(166, 288):
            flag = False
            # 随机种子，保证和第一次训练是相同的
            np.random.seed(i)
            start_point = np.random.randint(0, 800)
            if start_point in error_point:
                continue
            count += 1
            end_point = np.random.randint(801, 1725)
            print(start_point, '-->', end_point)

            # 读取已经存在本地的Q表
            df_q_table = pd.read_csv(
                os.getcwd() + '/table_' + str(self.omega) + '/' + configuration.CITY + '_' +
                str(start_point) + '_' + str(end_point) + '_' + 'q_table.csv', encoding="utf-8")
            # print(os.getcwd() + '/table_' + str(self.omega) + '/' + configuration.CITY + '_' +
            #       str(start_point) + '_' + str(end_point) + '_' + 'q_table.csv')
            df_q_table = df_q_table.set_index(['Unnamed: 0'])
            df_q_table = df_q_table[['1', '2', '3', '4']].astype(np.float64)

            RL = QLearningTable(self.actions)

            RL.gamma = 1
            # print(self.omega)
            # 贪心策略设置为1
            # RL.epsilon = 0.95

            # 更换Q表
            RL.q_table = df_q_table

            env = Cross_2th(self.next_state_list, self.action_list, self.distance_list, start_point, end_point,
                            self.cross_info, self.tel_list, self.df_tel, self.omega)
            # update block
            # for循环计数
            index_for = 0
            # for循环内延迟总和计算平均值
            delay_for_sum = 0
            transfer_for_sum = 0
            queue_for_sum = 0
            process_for_sum = 0
            for episode in range(10):
                # import SA
                T = 1000
                epsilon, T = tools.SA(T, episode, 10, 0.95)
                RL.epsilon = epsilon
                if epsilon > 1:
                    print("yes")
                # print(epsilon)
                one_episode_start_time = time.time()
                # 画图
                # plt.ion()
                observation = env.start_point
                prior_state = observation
                # while循环计数
                index_while = 0
                # while循环内延迟总和计算平均值
                delay_while_sum = 0
                transfer_while_sum = 0
                queue_while_sum = 0
                process_while_sum = 0
                while True:
                    index = RL.choose_action(observation, env, 2)
                    observation_, reward, done, tel_delay, transfer_time, queue_time, process_time = \
                        env.step_2th(observation, index, prior_state)

                    # print("observation_:", observation_, "observation:", observation, "prior_state:", prior_state)

                    index_while += 1
                    delay_while_sum += tel_delay
                    transfer_while_sum += transfer_time
                    queue_while_sum += queue_time
                    process_while_sum += process_time

                    # 陷入局部最优跳出
                    current_time = time.time()
                    if current_time - one_episode_start_time > 10:
                        flag = True
                        e_count += 1
                        print('error:', start_point, 'x--x', end_point)
                        # if observation not in error_list:
                        #     error_list.append(start_point)
                        break

                    # 画图部分
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
                    # plt.pause(0.1)
                    # plt.ioff()
                    #
                    df_q_table = RL.learn(observation, index, reward, observation_, 2)
                    # print(q_table[
                    #       q_table.index.values.tolist().index(str(29)):q_table.index.values.tolist().index(
                    #           str(29)) + 1])
                    # print(q_table[
                    #       q_table.index.values.tolist().index(str(77)):q_table.index.values.tolist().index(
                    #           str(77)) + 1])

                    prior_state = observation
                    observation = observation_
                    current_time = time.time()
                    if done:
                        break

                delay_while_avg = delay_while_sum / index_while
                transfer_while_avg = transfer_while_sum / index_while
                queue_while_avg = queue_while_sum / index_while
                process_while_avg = process_while_sum / index_while

                index_for += 1
                delay_for_sum += delay_while_avg
                transfer_for_sum += transfer_while_avg
                queue_for_sum += queue_while_avg
                process_for_sum += process_while_avg
                one_episode_end_time = time.time()
                # print('==========================================')
                # print(episode + 1, "th episode is completed, time cost:", one_episode_end_time - one_episode_start_time)
                # print('==========================================')
                # print(q_table)
                if flag:
                    break
            delay_avg = delay_for_sum / index_for
            transfer_avg = transfer_for_sum / index_for
            queue_avg = queue_for_sum / index_for
            process_avg = process_for_sum / index_for
            # print('transfer_avg is:', transfer_avg, 'queue_avg is:', queue_avg, 'process_avg is:', process_avg)
            delay_df = delay_df.append({'s_e': str(start_point) + '_' + str(end_point),
                                        'start_point': start_point,
                                        'end_point': end_point,
                                        'transfer': transfer_avg,
                                        'queue': queue_avg,
                                        'process': process_avg},
                                       ignore_index=True)
            # print('======================================================================')
            # print(delay_df)
            dir_path = os.getcwd() + '/table_realtime_Ω_' + str(self.omega) + '_ts_' + str(
                configuration.TASK_SIZE) + '_cc_' + str(configuration.CPU_CLOCK) + '_vp_' + str(
                configuration.VEHICLE_POWER)
            # print(dir_path)
            if 1 - bool(os.path.exists(dir_path)):
                os.makedirs(dir_path)
                os.makedirs(dir_path + '/time_cost/')
            df_q_table.to_csv(dir_path + '/' + configuration.CITY + '_' + str(start_point) + '_' + str(
                end_point) + '_realtime_q_table.csv', encoding="utf-8")
            delay_df.to_csv(dir_path + '/time_cost/' + 'TASK_SIZE_' + str(configuration.TASK_SIZE) + '_CPU_CLOCK_' +
                            str(configuration.CPU_CLOCK) + '_VEHICLE_POWER_' + str(configuration.VEHICLE_POWER) +
                            '_time_cost.csv', encoding="utf-8")
        #     跳出z循环
        #     if count - e_count == 5*(z+1):
        #         break
        time_end = time.time()
        time_cost = time_end - time_start - e_count * 10
        c_minus = count - e_count
        # cost_pre = time_cost*(round(10/(count-e_count), 3))
        print('totally completely, time cost:', time_cost)
        # print(c_minus)
        # print(cost_pre)
        print('==========================================')
        cost_list.append(time_cost)
        print(cost_list)
