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

    def step(self, state, index, index_flag):
        if index_flag:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            s_ = self.get_next_state(state, index)
            angle_1 = tools.getDegree(self.cross_info[state][5], self.cross_info[state][6],
                                      self.cross_info[self.end_point][5], self.cross_info[self.end_point][6])
            angle_2 = tools.getDegree(self.cross_info[state][5], self.cross_info[state][6],
                                      self.cross_info[self.next_state_list[state][index]][5], self.cross_info[self.next_state_list[state][index]][6])
            if s_ == self.end_point:
                reward = 1
                done = True
                s_ = 'end_point'
                print('get it')
            elif 100 < abs(angle_1 - angle_2) < 260:
                reward = -(1 / self.get_distance(state, index))
                done = False
            else:
                reward = 1 / self.get_distance(state, index)
                done = False
        return s_, reward, done


    # def get_node_order(self, q_table):
    #
    #     start = q_table.[q_table.loc[self.start_point, :].max()].index
    #     print(start)
    #     pass
