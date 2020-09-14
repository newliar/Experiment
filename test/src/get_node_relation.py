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
        angle_1 = tools.getDegree(cross_info[re_sort_[0][0]][5], cross_info[re_sort_[0][0]][6],
                                  cross_info[re_sort_[0][1]][5], cross_info[re_sort_[0][1]][6])
        for re_sort_ele in re_sort_:
            angle_2 = tools.getDegree(cross_info[re_sort_ele[0]][5], cross_info[re_sort_ele[0]][6],
                                      cross_info[re_sort_ele[1]][5], cross_info[re_sort_ele[1]][6])
            if abs(angle_1 - angle_2) >= 90:
                relation_.append(re_sort_[0])
                relation_.append(re_sort_ele)
                relation.append(relation_)
                break
            if angle_2 == tools.getDegree(cross_info[re_sort_ele[0]][5], cross_info[re_sort_ele[0]][6],
                                          cross_info[re_sort_[len(re_sort_) - 1][1]][5],
                                          cross_info[re_sort_[len(re_sort_) - 1][1]][6]):
                relation_.append(re_sort_[0])
                relation.append(relation_)
                break

    return distance, re, re_sort, relation


def write_relation_to_csv(relation):
    # relation的index范围为0-558
    relation_558 = []
    for i in range(559):
        same_node = []
        for relation_ in relation:
            if relation_[0][0] == i:
                for relation_ele in relation_:
                    same_node.append(relation_ele)
            if relation_[0][0] > i:
                break
        relation_558.append(same_node)
    relation_file = []
    for single_relation in relation_558:
        relation_file_ = [single_relation[0][0]]
        for ele in single_relation:
            # 添加target, way_id, way_name, distance, direction
            relation_file_.append(ele[1])
            relation_file_.append(ele[2])
            relation_file_.append(ele[3])
            relation_file_.append(ele[4])
            relation_file_.append(get_direction(cross_info[ele[0]][5], cross_info[ele[0]][6],
                                                cross_info[ele[1]][5], cross_info[ele[1]][6]))
        relation_file.append(relation_file_)
    df = pd.DataFrame(relation_file,
                      columns=[
                          'start_point',
                          'target_point_one', 'way_id_one', 'way_name_one', 'distance_one', 'direction_one',
                          'target_point_two', 'way_id_two', 'way_name_two', 'distance_two', 'direction_two',
                          'target_point_three', 'way_id_three', 'way_name_three', 'distance_three', 'direction_three',
                          'target_point_four', 'way_id_four', 'way_name_four', 'distance_four', 'direction_four'
                      ])
    df.to_csv('cross_relation.csv', index=False, encoding="utf-8")


if __name__ == "__main__":
    file_path = "cross_info.csv"
    df = pd.read_csv(file_path, encoding="utf-8")
    cross_info = round(df, 7).values.tolist()
    distance, re, re_sort, relation = get_shortest_node_on_same_way(cross_info)
    # write_relation_to_csv(relation)
    tools.draw_relation(relation, cross_info)
