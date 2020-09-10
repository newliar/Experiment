from RL_brain import QLearningTable
from cross_env import Cross
import tools
import pandas as pd
import numpy as np

N_STATES = 559
ACTIONS = ['u', 'd', 'l', 'r']


def update(env):
    for episode in range(100):
        observation = env.start_point
        while True:
            index, index_ = RL.choose_action(observation, env)

            observation_, reward, done = env.step(observation, index)

            RL.learn(observation, index, reward, observation_, index_)

            # observation_, reward, done =


if __name__ == "__main__":
    df = pd.read_csv('cross_relation.csv', encoding='utf-8')
    cross_info = tools.get_cross_info(df)
    next_state_list, distance_list, action_list = tools.get_details(cross_info)

    # TODO Start_Point & End_Point 待输入
    start_point = 0
    end_point = 559

    env = Cross(next_state_list, action_list, distance_list, start_point, end_point)
    RL = QLearningTable(ACTIONS)