import numpy as np
import pandas as pd
import os
import time
import matplotlib.pyplot as plt

import configuration
import tools
from RL_brain import QLearningTable
from cross_env import Cross


class UpdateRealtime:

    def __init__(self, actions, df_re, df_co, x, y, cross_relation, cross_info, next_state_list, distance_list,
                 action_list):
        self.actions = actions
        self.df_re = df_re
        self.df_co = df_co
        self.x = x
        self.y = y
        self.cross_relation = cross_relation
        self.cross_info = cross_info
        self.next_state_list = next_state_list
        self.distance_list = distance_list
        self.action_list = action_list

    def update_realtime(self):
        # TODO Start_Point & End_Point 待输入
        for i in range(166, 288):

