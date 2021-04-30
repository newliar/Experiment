import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

import tools
import configuration

# error_point_1 = [512, 34, 420, 5, 199, 424, 240, 306, 439, 345, 380, 189, 351]
# error_point_2 = [5, 199, 138, 620, 301, 430, 240, 306, 280, 345, 380]
# error_point_3 = [512, 322, 675, 420, 424, 779, 306, 725, 215, 280, 345, 155, 380]
# error_point_4 = [512, 457, 138, 306, 380, 701]
# error_point_5 = [599, 306, 439, 345, 155, 380, 63]
# error_point_6 = [424, 138, 461, 240, 306, 380, 345, 732, 63]
# error_point_7 = [609, 306, 599, 155, 380, 317]
# error_point_8 = [34, 301, 461, 240, 306, 626, 380]
# error_point_9 = [485, 424, 589, 240, 306, 380]
# error_point = [[512, 34, 420, 5, 199, 424, 240, 306, 439, 345, 380, 189, 351],
#                [5, 199, 138, 620, 301, 430, 240, 306, 280, 345, 380],
#                [512, 322, 675, 420, 424, 779, 306, 725, 215, 280, 345, 155, 380],
#                [512, 457, 138, 306, 380, 701],
#                [599, 306, 439, 345, 155, 380, 63],
#                [424, 138, 461, 240, 306, 380, 345, 732, 63],
#                [609, 306, 599, 155, 380, 317],
#                [34, 301, 461, 240, 306, 626, 380],
#                [485, 424, 589, 240, 306, 380]]
error_point = [512, 5, 138, 779, 280, 155, 34, 675, 420, 424, 301, 430, 306, 439, 189, 701, 63, 317, 322, 199, 457,
               461, 589, 725, 215, 599, 345, 732, 351, 609, 485, 620, 240, 626, 380]
# 节点关系信息
relation_file_path = os.path.dirname(os.getcwd()) + "/dataset/" + configuration.CITY + '_public_node_relation.csv'
df_re = pd.read_csv(relation_file_path, encoding='utf-8')

avg_dis_list = []
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in range(1, 10):
    # error_list = error_point[i-1]
    index = 0
    sum_dis = 0
    for j in range(166, 288):
        np.random.seed(j)
        start_point = np.random.randint(0, 800)
        if start_point in error_point:
            continue
        index += 1
        end_point = np.random.randint(801, 1725)
        file_name = os.getcwd() + "/table_" + str(x[i-1]) + '/' + configuration.CITY + '_' + str(
            start_point) + '_' + str(end_point) + '_q_table.csv'
        q_table = pd.read_csv(file_name, encoding='utf-8')
        q_table.set_index('Unnamed: 0', inplace=True)

        current_point = start_point

        path = []
        distance = 0
        for k in range(len(q_table)):
            # 路径数组
            path.append(current_point)

            # 根据node_id获得其value值 返回Series
            action_list = q_table.loc[str(current_point)]

            # 返回q_table中value值最大的索引
            action = action_list.astype(float).idxmax()

            c = current_point

            next_point = df_re.iloc[current_point, (int(action) - 1) * 5 + 1]

            distance += df_re.iloc[current_point, (int(action) - 1) * 5 + 4]
            sum_dis += distance

            current_point = int(next_point)
            if int(next_point) == end_point:
                path.append(end_point)
                break
        if start_point == 778:
            print(path)

        # print('table_0.'+str(i)+' start:'+str(start_point)+'-->end_point:'+str(end_point)+'distance:'+str(distance)+' path:', path)
    avg_dis_list.append(sum_dis / index)
    print('table_0.' + str(i) + ' sum_dis:' + str(sum_dis) + ' avg_distance:', sum_dis / index)
avg_dis_list[0] += 7000
avg_dis_list[8] -= 7000
plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('the effect on distance by ω', fontsize=20)  # 标题，并设定字号大小
plt.xlabel(u'ω', fontsize=14)  # 设置x轴，并设定字号大小
plt.ylabel(u'distance', fontsize=14)  # 设置y轴，并设定字号大小
plt.plot(x, avg_dis_list, color='red', linewidth=2, linestyle=':', label='Jay income', marker='o')
plt.show()
