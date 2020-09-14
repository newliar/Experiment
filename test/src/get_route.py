from RL_brain import QLearningTable
from cross_env import Cross
import tools
import pandas as pd
import numpy as np
import time

N_STATES = 559
ACTIONS = ['u', 'd', 'l', 'r']


def update(env):
    # time_start = time.time()
    for episode in range(1000):
        time_start = time.time()
        observation = env.start_point
        while True:
            index, index_flag = RL.choose_action(observation, env)

            observation_, reward, done = env.step(observation, index, index_flag)

            q_table = RL.learn(observation, index, reward, observation_, env)

            observation = observation_

            if done:
                break
        time_end = time.time()
        print(episode + 1, "th episode is completed, totally cost:", time_end - time_start)
        print('--------------------------------------------------------')
        print(q_table)
        print('--------------------------------------------------------')
    # time_end = time.time()
    print('over', time_end - time_start)
    return q_table


if __name__ == "__main__":
    df_re = pd.read_csv('cross_relation.csv', encoding='utf-8')
    df_co = pd.read_csv('cross_info.csv', encoding='utf-8')
    cross_relation = tools.get_cross_info(df_re)
    cross_info = df_co.values.tolist()
    next_state_list, distance_list, action_list = tools.get_details(cross_relation)

    # TODO Start_Point & End_Point 待输入
    start_point = 252
    end_point = 497

    RL = QLearningTable(ACTIONS)
    env = Cross(next_state_list, action_list, distance_list, start_point, end_point, cross_info)
    q_table = update(env)
    # env.get_node_order(q_table)