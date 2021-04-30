import tools
import traceback
import numpy as np
import choose_tel
from choose_tel import Choose
import math
import configuration


class Cross_2th:
    def __init__(self, next_state_list, action_list, distance_list, start_point, end_point, cross_info, tel_list, df_tel, omega, n_states=1724):
        self.next_state_list = next_state_list
        self.action_list = action_list
        self.distance_list = distance_list
        self.start_point = start_point
        self.end_point = end_point
        self.cross_info = cross_info
        self.tel_list = tel_list
        self.n_states = n_states
        self.df_tel = df_tel
        self.omega = omega

    def get_next_states(self, state):
        return self.next_state_list[state]

    def get_next_state(self, state, index):
        # print(self.next_state_list[state])
        return self.next_state_list[state][index]

    def get_distance(self, state, index):
        return self.distance_list[state][index]

    def get_tels(self, state, index):
        return self.cross_info[self.get_next_state(state, index)][12]

    def get_length(self, state):
        try:
            state = int(state)
            return len(self.action_list[state])
        except Exception as ex:
            print(state)
            print('#########')
            print(ex.args)
            print('#########')
            print(traceback.format_exc())

    def step_2th(self, state, index, prior_state):
        s_ = self.get_next_state(state, index)
        # print('s_:', s_)

        # 获得终点相较于当前状态的方位角
        azimuth_4 = tools.getDegree(self.cross_info[state][1], self.cross_info[state][2],
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
                                       self.cross_info[self.start_point][1], self.cross_info[self.start_point][2])

        # azimuth_4和azimuth_6的夹角
        angle = tools.get_angle(azimuth_4, azimuth_6)

        # 随机任务大小(10-100MB)
        np.random.seed(state)
        # task_size = np.random.randint(10, 100)
        ch = Choose()

        # 获得下一个状态范围内的基站并随机选择一个用来模拟延迟最小
        tel_list = self.tel_list[self.get_next_state(state, index)]
        # print(tel_list, '----', state, '-----', index, 'length', len(tel_list), 'type', type(tel_list))
        # 如果数据集提供的数据在此范围无基站,自行生成基站和延迟
        if len(tel_list) == 2:
            # print(tel_list)
            # tel = 7
            # tel_delay_list = self.df_tel.iloc[int(tel), 3]
            transfer_time = configuration.TASK_SIZE/(20 * math.log(1 + (configuration.VEHICLE_POWER * (127 + 30 * math.log(200, 10))) / 0.002, 2))*1000
            queue_time = choose_tel.get_queue_time()
            process_time = configuration.TASK_SIZE/configuration.CPU_CLOCK
            tel_delay = transfer_time + queue_time + process_time
            # print('空基站', tel_delay, 'task_size', task_size, 'transfer_time', transfer_time)
        else:
            tel_list = tel_list[1:-1]
            tel_list = tel_list.split(',')
            tel_delay = 999999
            for tel in tel_list:
                transfer_time = ch.get_transfer_time(configuration.TASK_SIZE, state, int(tel))
                # queue_time = choose_tel.get_queue_time()
                # print(tel_list)
                queue_time = choose_tel.get_real_queue(df_tel=self.df_tel, tel=int(tel))
                process_time = choose_tel.get_process_time(configuration.TASK_SIZE, int(tel))
                if tel_delay > transfer_time + queue_time + process_time:
                    tel_delay = transfer_time + queue_time + process_time
            # print('实际基站', tel_delay)
            # print(transfer_time+queue_time+process_time)
            # tel = np.random.choice(tel_list)
            # tel_delay_list = self.df_tel.iloc[int(tel), 3]

        # tel_delay_list = tel_delay_list[1:-1]
        # if tel_delay_list[0] == ' ':
        #     tel_delay_list = tel_delay_list[1:]
        # tel_delay_list = tel_delay_list.replace('  ', ' ')
        # tel_delay_list = tel_delay_list.split(' ')
        # 在延迟列表中随机选择一个作为延迟
        # tel_delay = transfer_time+queue_time+process_time
        # print(tel_list)

        # total_cost_pre = 0.8*self.get_distance(state, index) + 0.2*20*10
        # total_cost = 0.8*self.get_distance(state, index) + 0.2*20*(tel_delay-10)
        # gap = total_cost - total_cost_pre
        # print(tel_delay)
        distance = self.get_distance(state, index)
        # 权重设置
        total_cost = self.omega/5*distance+(1-self.omega)/5*(tel_delay-10)
        # print(total_cost)
        # print('distance is', distance, 'and tel_delay is', tel_delay, 'and total cost is', total_cost)
        # 如果到达终点，返回奖励1，并给予完成状态
        if s_ == prior_state:
            # print("loop s_:", s_, "<--> prior_state:", prior_state)
            reward = -0.5
            done = False
        elif s_ == self.end_point:
            reward = 1
            done = True
            s_ = 'end_point'
            # print('get it')
        # 靠近终点正向奖励
        elif distance_2 < distance_3 and angle < 50:
            if total_cost == 0:
                reward = 0
            else:
                reward = 1 / total_cost
            done = False
        # 远离终点惩罚
        elif distance_2 > distance_3:
            if total_cost == 0:
                reward = 0
            else:
                reward = -2 / total_cost
            done = False
        # 如果下一状态到终点的直线距离两倍于起点到终点的直线距离，跳出循环
        elif distance_2 > distance_1 * 1.5:
            if total_cost == 0:
                reward = 0
            else:
                reward = -1
            done = True
            s_ = 'terminal'
        # 如果所选下一个action与终点角度差距过大，惩罚
        elif 120 < abs(azimuth_6 - azimuth_4) < 260:
            if total_cost == 0:
                reward = 0
            else:
                reward = -2 / total_cost
            done = False
        # 超距后，惩罚
        elif distance_1 < distance_5:
            if total_cost == 0:
                reward = 0
            else:
                reward = -3 / total_cost
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
            if total_cost == 0:
                reward = 0
            else:
                reward = -1 / total_cost
            done = False
        return s_, reward, done, tel_delay, transfer_time, queue_time, process_time
