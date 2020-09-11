import numpy as np
import pandas as pd
from cross_env import Cross


class QLearningTable:
    def __init__(self, actions, learning_rate=1, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation, env):
        self.check_state_exist(observation)
        length = env.get_length(observation)
        index_flag = False
        if np.random.uniform() < self.epsilon:
            state_action = self.q_table.loc[observation, :]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
            index = self.actions.index(action)
            if index > length - 1:
                index_flag = True
        else:
            action = np.random.choice(self.actions)
            index = self.actions.index(action)
            if index > length - 1:
                index_flag = True
        return index, index_flag

    def learn(self, s, i, r, s_, env):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, self.actions[i]]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r
        self.q_table.loc[s, self.actions[i]] += self.lr * (q_target - q_predict)
        # print('--------------------------------------------------------')
        # print(self.q_table)

        return self.q_table

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state
                )
            )
