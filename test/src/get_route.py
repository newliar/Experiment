from RL_brain import QLearningTable
from cross_env import Cross
import tools
import pandas as pd
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import os
import configuration

ACTIONS = ['1', '2', '3', '4']


def update(env, start_point, end_point):
    time_start = time.time()
    for episode in range(100):
        episode_start_time = time.time()
        plt.ion()
        observation = env.start_point
        # if episode >= 30:
        #     RL.epsilon = 1.0
        while True:
            index = RL.choose_action(observation, env)

            observation_, reward, done = env.step(observation, index)
            # print(observation_)
            
            plt.clf()
            plt.scatter(x[start_point], y[start_point], marker='o', s=100, label='start_point', c='yellow')
            plt.scatter(x[end_point], y[end_point], marker='^', s=100, label='end_point', c='yellow')
            plt.scatter(x, y, s=15, alpha=0.3, c='green')
            if observation_ == 'end_point':
                plt.scatter(x[end_point], y[end_point], s=15, c='red')
            elif observation_ == 'terminal':
                plt.scatter(x[observation], y[observation], s=15, c='yellow')
            else:
                plt.scatter(x[observation_], y[observation_], s=15, c='red')
            plt.pause(0.01)
            plt.ioff()

            q_table = RL.learn(observation, index, reward, observation_, env)

            observation = observation_
            current_time = time.time()
            if current_time - episode_start_time > 180:
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
    return q_table


def update_realtime():
    for episode in range(100):
        observation = env.start_point
        RL.e_greedy = 1
        RL.q_table = q_table
        while True:
            index = RL.choose_action(observation, env)


if __name__ == "__main__":
    df_re = pd.read_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_relation.csv', encoding='utf-8')
    df_co = pd.read_csv(os.path.dirname(os.getcwd())+"/dataset/"+configuration.CITY+'_public_node_info_.csv', encoding='utf-8')
    x = df_co['lon'].round(decimals=6).tolist()
    y = df_co['lat'].round(decimals=6).tolist()
    cross_relation = tools.get_cross_info(df_re)
    cross_info = df_co.values.tolist()
    next_state_list, distance_list, action_list, tel_list = tools.get_details(cross_relation)

    # TODO Start_Point & End_Point 待输入
    for i in range(66, 88):
        np.random.seed(i)
        start_point = np.random.randint(0, 800)
        end_point = np.random.randint(801, 1725)
        RL = QLearningTable(ACTIONS)
        env = Cross(next_state_list, action_list, distance_list, start_point, end_point, cross_info)
        q_table = update(env, start_point, end_point)
        q_table.to_csv(os.getcwd()+'/table/'+configuration.CITY+'_'+str(start_point)+'_'+str(end_point)+'_'+'q_table.csv', encoding="utf-8")
    # df_q_tb = pd.read_csv(os.getcwd() + '/table/0_363_q_table.csv', encoding='utf-8')
    # q_table = df_q_tb.values.tolist()
                

