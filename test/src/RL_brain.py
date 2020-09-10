import numpy as np
import pandas as pd
from cross_env import Cross


class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation, env):
        self.check_state_exist(observation, env)
        length = env.get_length(observation)
        if np.random.uniform() < self.epsilon:
            state_action = self.q_table.loc[observation, self.actions[0:length]]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
            index = self.actions[action].index
        else:
            action = np.random.choice(self.actions[0:length])
            index = self.actions[action].index
        return index

    def learn(self, s, i, r, s_, i_):
        # TODO:不能之间加减 Q 表，必须取到对应元素 e.g. 新 Q(s1,a2) = 老 Q(s1,a2) + α * 差距      差距=现实-估计
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, self.actions[i]]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, self.actions[i_]].max()
        else:
            q_target = r
        self.q_table.loc[s, self.actions[i]] += self.lr * (q_target - q_predict)

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state
                )
            )
