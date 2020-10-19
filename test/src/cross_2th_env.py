import tools
import traceback
import numpy as np


class Cross_2th:
    def __init__(self, next_state_list, action_list, distance_list, start_point, end_point, cross_info, tel_list, n_states=1724):
        self.next_state_list = next_state_list
        self.action_list = action_list
        self.distance_list = distance_list
        self.start_point = start_point
        self.end_point = end_point
        self.cross_info = cross_info
        self.tel_list = tel_list
        self.n_states = n_states

    def get_next_states(self, state):
        return self.next_state_list[state]

    def get_next_state(self, state, index):
        return self.next_state_list[state][index]

    def get_distance(self, state, index):
        return self.distance_list[state][index]

    def get_tels(self, state, index):
        return self.cross_info[self.get_next_state(state, index)][12]

    def get_length(self, state):
        try:
            return len(self.action_list[state])
        except Exception as ex:
            print(state)
            print('#########')
            print(ex.args)
            print('#########')
            print(traceback.format_exc())

    def step_2th(self, state, index):
        s_ = self.get_next_state(state, index)

        # 获得终点相较于当前状态的方位角
        azimuth_4 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
                                    self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 获得下一节点相较于当前状态的方位角
        azimuth_6 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
                                    self.cross_info[self.next_state_list[state][index]][1],
                                    self.cross_info[self.next_state_list[state][index]][2])

        # azimuth_4和azimuth_6的夹角
        angle = tools.get_angle(azimuth_4, azimuth_6)

        # 获得下一个状态范围内的基站并随机选择一个用来模拟延迟最小
        tel = np.random.choice(self.tel_list[self.get_next_state(state, index)])
