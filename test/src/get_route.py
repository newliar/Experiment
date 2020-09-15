from RL_brain import QLearningTable
from cross_env import Cross
import tools
import pandas as pd
import time

ACTIONS = ['1', '2', '3', '4', '5', '6']


def update(env):
    time_start = time.time()
    for episode in range(100000):
        time_start = time.time()
        observation = env.start_point
        while True:
            index = RL.choose_action(observation, env)

            observation_, reward, done = env.step(observation, index)

            q_table = RL.learn(observation, index, reward, observation_, env)

            observation = observation_

            if done:
                break
        print('==========================================')
        print(episode + 1, "th episode is completed")
        print('==========================================')
        print(q_table)
    time_end = time.time()
    print('totally completely, time cost:', time_end - time_start)
    return q_table


if __name__ == "__main__":
    df_re = pd.read_csv('public_node_relation.csv', encoding='utf-8')
    df_co = pd.read_csv('public_node_info_.csv', encoding='utf-8')
    cross_relation = tools.get_cross_info(df_re)
    cross_info = df_co.values.tolist()
    next_state_list, distance_list, action_list = tools.get_details(cross_relation)

    # TODO Start_Point & End_Point 待输入
    start_point = 521
    end_point = 309

    RL = QLearningTable(ACTIONS)
    env = Cross(next_state_list, action_list, distance_list, start_point, end_point, cross_info)
    q_table = update(env)
