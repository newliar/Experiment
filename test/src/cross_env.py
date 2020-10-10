import tools
import traceback


class Cross:
    def __init__(self, next_state_list, action_list, distance_list, start_point, end_point, cross_info, n_states=559):
        self.next_state_list = next_state_list
        self.action_list = action_list
        self.distance_list = distance_list
        self.start_point = start_point
        self.end_point = end_point
        self.cross_info = cross_info
        # self.tel_list = tel_list
        self.n_states = n_states

    def get_next_states(self, state):
        return self.next_state_list[state]

    def get_next_state(self, state, index):
        return self.next_state_list[state][index]

    def get_distance(self, state, index):
        return self.distance_list[state][index]

    def get_tels(self, state, index):
        return self.tel_list[state][index]

    def get_length(self, state):
        try:
            return len(self.action_list[state])
        except Exception as ex:
            print(state)
            print('#########')
            print(ex.args)
            print('#########')
            print(traceback.format_exc())

    def step(self, state, index):
        s_ = self.get_next_state(state, index)

        # 获得终点相对于起点的方位角
        azimuth_1 = tools.getDegree(self.cross_info[self.start_point][1], self.cross_info[self.start_point][2],
                                    self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 获得当前状态相较于起点的方位角
        azimuth_2 = tools.getDegree(self.cross_info[self.start_point][1], self.cross_info[self.start_point][2],
                                    self.cross_info[state][1], self.cross_info[state][2])

        # 获得下一状态相较于起点的方位角
        azimuth_3 = tools.getDegree(self.cross_info[self.start_point][1], self.cross_info[self.start_point][2],
                                    self.cross_info[self.next_state_list[state][index]][1],
                                    self.cross_info[self.next_state_list[state][index]][2])

        # 获得终点相较于当前状态的方位角
        azimuth_4 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
                                    self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 获得终点相对于下一状态的方位角
        azimuth_5 = tools.getDegree(self.cross_info[self.next_state_list[state][index]][1],
                                    self.cross_info[self.next_state_list[state][index]][2],
                                    self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 获得下一节点相较于当前状态的方位角
        azimuth_6 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
                                    self.cross_info[self.next_state_list[state][index]][1],
                                    self.cross_info[self.next_state_list[state][index]][2])

        # 获得起点与终点的直线距离
        distance_1 = tools.geodistance(self.cross_info[self.start_point][1], self.cross_info[self.start_point][2],
                                       self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 获得下一状态与终点之间的距离
        distance_2 = tools.geodistance(self.cross_info[self.next_state_list[state][index]][1],
                                       self.cross_info[self.next_state_list[state][index]][2],
                                       self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 当前状态与终点之间的距离
        distance_3 = tools.geodistance(self.cross_info[state][1], self.cross_info[state][2],
                                       self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])

        # 当前状态与起点之间的距离
        distance_4 = tools.geodistance(self.cross_info[state][1], self.cross_info[state][2],
                                       self.cross_info[self.start_point][1], self.cross_info[self.start_point][2])

        # 下一状态与起点之间的距离
        distance_5 = tools.geodistance(self.cross_info[self.next_state_list[state][index]][1],
                                       self.cross_info[self.next_state_list[state][index]][2],
                                       self.cross_info[self.start_point][1], self.cross_info[self.start_point][2]
                                       )

        # azimuth_4和azimuth_6的夹角
        angle = tools.get_angle(azimuth_4, azimuth_6)

        # 如果到达终点，返回奖励1，并给予完成状态
        if s_ == self.end_point:
            reward = 1
            done = True
            s_ = 'end_point'
            print('get it')
        # 靠近终点正向奖励
        elif distance_2 < distance_3 and angle < 50:
            reward = 1 / self.get_distance(state, index)
            done = False
        # 远离终点惩罚
        elif distance_2 > distance_3:
            reward = -(2 / self.get_distance(state, index))
            done = False
        # 如果下一状态到终点的直线距离两倍于起点到终点的直线距离，跳出循环
        elif distance_2 > distance_1 * 1.5:
            reward = -1
            done = True
            s_ = 'terminal'
        # 如果所选下一个action与终点角度差距过大，惩罚
        elif 120 < abs(azimuth_6 - azimuth_4) < 260:
            reward = -(2 / self.get_distance(state, index))
            done = False
        # 超距后，惩罚
        elif distance_1 < distance_5:
            reward = -(3 / self.get_distance(state, index))
            done = False
        # elif distance_2 > distance_3:
        #     reward = -(2 / self.get_distance(state, index))
        #     done = False
        # elif (abs(angle_1 - angle_3) < 60 or 300 < abs(360 - (angle_1 - angle_3)) < 360) and \
        #         (abs(angle_1 - angle_2) or 300 < abs(360 - (angle_1 - angle_3)) < 360) and \
        #         distance_2 < distance_1 and distance_2 < distance_3:
        #     reward = 1 / self.get_distance(state, index)
        #     done = False
        # elif abs(angle_1-angle_3) < 60 or abs(360-(angle_1-angle_3)) < 60:
        #     reward = 1 / self.get_distance(state, index)
        #     done = False
        else:
            reward = -(1 / self.get_distance(state, index))
            done = False
        return s_, reward, done

    # def step_second(self, state, index):
    #     s_ = self.get_next_state(state, index)
    #     tel_list = self.get_tels(state, index)
    #     tel_len = len(tel_list)
    #     if tel_len == 0:
