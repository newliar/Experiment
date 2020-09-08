import pandas as pd
import tools


def get_direction(lonA, latA, lonB, latB):
    dire_arr = ['up', 'right_up', 'right', 'right_down', 'down', 'left_down', 'left', 'left_up']
    angle = tools.getDegree(lonA, latA, lonB, latB)
    if (0 <= angle < 22.5) or (337.5 <= angle < 360):
        direction = dire_arr[0]
    elif 22.5 <= angle < 67.5:
        direction = dire_arr[1]
    elif 67.5 <= angle < 112.5:
        direction = dire_arr[2]
    elif 112.5 <= angle < 157.5:
        direction = dire_arr[3]
    elif 157.5 <= angle < 202.5:
        direction = dire_arr[4]
    elif 202.5 <= angle < 247.5:
        direction = dire_arr[5]
    elif 247.5 <= angle < 292.5:
        direction = dire_arr[6]
    elif 292.5 <= angle < 337.5:
        direction = dire_arr[7]
    return direction


def get_shortest_node_on_same_way(cross_info):
    relation = []
    distance = []
    # 获得way_name相同的路口之间的距离
    for node in cross_info:
        distance_ = []
        for node_compare in cross_info:
            if node[0] == node_compare[0]:
                continue
            else:
                if node[2] == node_compare[2]:
                    distance_ = [node[0], node_compare[0], node[1], node[2],
                                 tools.geodistance(node[5], node[6], node_compare[5],
                                                   node_compare[6])]
                    distance.append(distance_)
                if node[2] == node_compare[4]:
                    distance_ = [node[0], node_compare[0], node[1], node[2],
                                 tools.geodistance(node[5], node[6], node_compare[5],
                                                   node_compare[6])]
                    distance.append(distance_)
                if node[4] == node_compare[2]:
                    distance_ = [node[0], node_compare[0], node[3], node[4],
                                 tools.geodistance(node[5], node[6], node_compare[5],
                                                   node_compare[6])]
                    distance.append(distance_)
                if node[4] == node_compare[4]:
                    distance_ = [node[0], node_compare[0], node[3], node[4],
                                 tools.geodistance(node[5], node[6], node_compare[5],
                                                   node_compare[6])]
                    distance.append(distance_)
    re = []
    way_name = []
    # 路口按照way_name归类
    for ele in distance:
        if [ele[0], ele[3]] not in way_name:
            way_name.append([ele[0], ele[3]])
    for i in range(len(way_name)):
        re_ = []
        for ele in distance:
            if way_name[i] == [ele[0], ele[3]]:
                re_.append(ele)
        re.append(re_)

    # 按照距离从小到大排序
    re_sort = []
    for ele in re:
        in_x = []
        temp = []
        for ele_ in ele:
            in_x.append(ele_[4])
        in_x.sort()
        if len(in_x) == 0:
            print("*****")
            continue
        elif len(in_x) == 1:
            re_sort.append(ele)
            continue
        elif len(in_x) >= 2:
            for x in in_x:
                for ele_ in ele:
                    if ele_[4] == x:
                        temp.append(ele_)
        re_sort.append(temp)

    for re_sort_ in re_sort:
        relation_ = []
        try:
            i = re_sort_[0][0]
            j = re_sort_[0][1]
        except:
            print(re_sort_)
        angle_1 = tools.getDegree(cross_info[re_sort_[0][0]][5], cross_info[re_sort_[0][0]][6],
                                  cross_info[re_sort_[0][1]][5], cross_info[re_sort_[0][1]][6])
        for re_sort_ele in re_sort_:
            angle_2 = tools.getDegree(cross_info[re_sort_ele[0]][5], cross_info[re_sort_ele[0]][6],
                                      cross_info[re_sort_ele[1]][5], cross_info[re_sort_ele[1]][6])
            if abs(angle_1-angle_2) >= 90:
                relation_.append(re_sort_[0])
                relation_.append(re_sort_ele)
        relation.append(relation_)



            # target_index = []
    # for ele in re:
    #     target_index_ = []
    #     for ele_ in ele:
    #         target_index_.append(ele_[1])
    #
    #     target_index.append(target_index_)
    #
    #
    # dependency = []
    # for i in range(len(re)):
    #     for ele_ in re[i]:
    #         for ele_compare in re:
    #             if re[i] == ele_compare:
    #                 continue
    #             if ele_[1] < ele_compare[0][0]:
    #                 break
    #             if ele_[1] == ele_compare[0][0]:
    #                 for ele_compare_ in ele_compare:
    #                     if ele_compare_[1] in target_index[i]:
    #                         if re[i][target_index[i].index(ele_compare_[1])][4] > ele_compare_[4]:
    #                             if re[i][target_index[i].index(ele_compare_[1])] not in dependency:
    #                                 dependency.append(re[i][target_index[i].index(ele_compare_[1])])
    #
    # raw_relation = []
    # for _re_ in re:
    #     raw_relation_ = []
    #     for re_ele in _re_:
    #         if re_ele not in dependency:
    #             raw_relation_.append(re_ele)
    #     raw_relation.append(raw_relation_)
    #
    # # 十字路口编号范围 0~558
    # for i in range(559):
    #     relation_ = []
    #     for raw_data in raw_relation:
    #         if len(raw_data) == 0:
    #             continue
    #         if raw_data[0][0] == i:
    #             for data in raw_data:
    #                 relation_.append(data)
    #     relation.append(relation_)
    #
    # # for ele in re_:
    # #     if len(ele) == 1:
    # #         way_id = ele[0][2]
    # #         way_name = ele[0][3]
    # #         for node in cross_info:
    # #             if (node[1] != way_id and node[2] == way_name) or (node[3] != way_id and node[4] == way_name):
    #
    # # for dependency_ele in dependency:
    # #     for re_sort_ele in re_sort:
    # #         for ele in re_sort_ele:
    # #             if ele == dependency_ele:
    # #                 re_sort_ele.remove(ele)

    return distance, re, re_sort, relation


def write_relation(raw_relation):
    relation = []
    for raw_relation in raw_relation:
        if len(raw_relation) != 0:
            relation.append(raw_relation)


if __name__ == "__main__":
    file_path = "cross_info.csv"
    df = pd.read_csv(file_path, encoding="gb2312")
    cross_info = round(df, 7).values.tolist()
    distance, re, re_sort, relation = get_shortest_node_on_same_way(cross_info)
