import numpy as np


class Cross:
    def __init__(self, next_state_list, action_list, distance_list, start_point, end_point, n_states=559):
        self.next_state_list = next_state_list
        self.action_list = action_list
        self.distance_list = distance_list
        self.start_point = start_point
        self.end_point = end_point
        self.n_states = n_states

    def get_next_states(self, state):
        return self.next_state_list[state]

    def get_next_state(self, state, index):
        return self.next_state_list[state][index]

    def get_distance(self, state, index):
        return self.distance_list[state][index]

    def get_length(self, state):
        return len(self.action_list[state])

    def step(self, state, index):
        s_ = self.get_next_state[state][index]
        if index == self.end_point:
            reward = 1
            done = True
            s_ = 'terminal'
        else:
            reward = 1 / self.get_distance[state][index]
            done = False
        return s_, reward, done
