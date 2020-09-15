import tools


class Cross:
    def __init__(self, next_state_list, action_list, distance_list, start_point, end_point, cross_info, n_states=559):
        self.next_state_list = next_state_list
        self.action_list = action_list
        self.distance_list = distance_list
        self.start_point = start_point
        self.end_point = end_point
        self.cross_info = cross_info
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
        s_ = self.get_next_state(state, index)
        # 获得终点相较于当前状态的方位角
        angle_1 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
                                  self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])
        # 获得下一节点相较于当前状态的方位角
        angle_2 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
                                  self.cross_info[self.next_state_list[state][index]][1], self.cross_info[self.next_state_list[state][index]][2])
        # 获得起点与终点的直线距离
        distance_1 = tools.geodistance(self.cross_info[self.start_point][1], self.cross_info[self.start_point][2],
                                       self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])
        # 获得下一状态与终点之间的距离
        distance_2 = tools.geodistance(self.cross_info[self.next_state_list[state][index]][1], self.cross_info[self.next_state_list[state][index]][2],
                                       self.cross_info[self.end_point][1], self.cross_info[self.end_point][2])
        # 如果到达终点，返回奖励1，并给予完成状态
        if s_ == self.end_point:
            reward = 10
            done = True
            s_ = 'end_point'
            print('get it')
        # 如果所选下一个action与终点角度差距过大，减少奖励
        elif 110 < abs(angle_1 - angle_2) < 250:
            reward = -(2 / self.get_distance(state, index))
            done = False
        # 如果下一状态到终点的直线距离两倍于起点到终点的直线距离，跳出循环
        elif distance_2 > distance_1*2:
            reward = -1
            done = True
            s_ = 'terminal'
        elif abs(angle_1 - angle_2) < 60 and distance_2 < distance_1:
            reward = 1 / self.get_distance(state, index)
            done = False
        else:
            reward = -(1 / self.get_distance(state, index))
            done = False
        return s_, reward, done
