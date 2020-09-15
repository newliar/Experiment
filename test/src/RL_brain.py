import numpy as np
import pandas as pd


class QLearningTable:
    def __init__(self, actions, learning_rate=1, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation, env):
        # 检查当前state是否存在于Q表
        self.check_state_exist(observation)
        # 获得当前状态的所有可用action的长度
        length = env.get_length(observation)
        # 当随机数小于epsilon时按Q表最大值执行，其他情况随机执行
        if np.random.uniform() < self.epsilon:
            # 获得当前状态可用的action，并不是所有state都有6个action
            state_action = self.q_table.loc[observation, self.actions[0:length]]
            # 获得所选action的index
            # np.random.choice的目的是当多个value值相同时随机选择一个，避免每次都是选第一个
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
            index = self.actions.index(action)
        else:
            # 随机选择一个当前state的可用action，并返回其action的index
            action = np.random.choice(self.actions[0:length])
            index = self.actions.index(action)
        return index

    def learn(self, s, i, r, s_, env):
        # 检查当前state是否存在于Q表
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, self.actions[i]]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r
        self.q_table.loc[s, self.actions[i]] += self.lr * (q_target - q_predict)

        return self.q_table

    # 查看此状态是否存在于Q表，不在即添加
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state
                )
            )
