import pandas as pd
import tools
import traceback


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

def get_shortest_node_by_same_id(public_node_info):
    distance = []
    for node in public_node_info:
        distance_ = []
        for node_compare in public_node_info:
            if node[0] == node_compare[0]:
                continue
            else:
                # 第一轮比较
                try:
                    if node[4] == node_compare[4]:
                        distance_ = [node[0], node_compare[0], int(node[4]), node[5],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[4] == node_compare[6]:
                        distance_ = [node[0], node_compare[0], int(node[4]), node[5],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[4] == node_compare[8]:
                        distance_ = [node[0], node_compare[0], int(node[4]), node[5],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[4] == node_compare[10]:
                        distance_ = [node[0], node_compare[0], int(node[4]), node[5],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[4] == node_compare[12]:
                        distance_ = [node[0], node_compare[0], int(node[4]), node[5],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[4] == node_compare[14]:
                        distance_ = [node[0], node_compare[0], int(node[4]), node[5],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)

                # 第二轮比较
                try:
                    if node[6] == node_compare[4]:
                        distance_ = [node[0], node_compare[0], int(node[6]), node[7],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[6] == node_compare[6]:
                        distance_ = [node[0], node_compare[0], int(node[6]), node[7],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[6] == node_compare[8]:
                        distance_ = [node[0], node_compare[0], int(node[6]), node[7],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[6] == node_compare[10]:
                        distance_ = [node[0], node_compare[0], int(node[6]), node[7],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[6] == node_compare[12]:
                        distance_ = [node[0], node_compare[0], int(node[6]), node[7],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[6] == node_compare[14]:
                        distance_ = [node[0], node_compare[0], int(node[6]), node[7],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)

                # 第三轮比较
                try:
                    if node[8] == node_compare[4]:
                        distance_ = [node[0], node_compare[0], int(node[8]), node[9],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[8] == node_compare[6]:
                        distance_ = [node[0], node_compare[0], int(node[8]), node[9],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[8] == node_compare[8]:
                        distance_ = [node[0], node_compare[0], int(node[8]), node[9],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[8] == node_compare[10]:
                        distance_ = [node[0], node_compare[0], int(node[8]), node[9],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[8] == node_compare[12]:
                        distance_ = [node[0], node_compare[0], int(node[8]), node[9],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[8] == node_compare[14]:
                        distance_ = [node[0], node_compare[0], int(node[8]), node[9],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)

                # 第四轮比较
                try:
                    if node[10] == node_compare[4]:
                        distance_ = [node[0], node_compare[0], int(node[10]), node[11],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[10] == node_compare[6]:
                        distance_ = [node[0], node_compare[0], int(node[10]), node[11],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[10] == node_compare[8]:
                        distance_ = [node[0], node_compare[0], int(node[10]), node[11],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[10] == node_compare[10]:
                        distance_ = [node[0], node_compare[0], int(node[10]), node[11],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[10] == node_compare[12]:
                        distance_ = [node[0], node_compare[0], int(node[10]), node[11],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[10] == node_compare[14]:
                        distance_ = [node[0], node_compare[0], int(node[10]), node[11],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)

                # 第五轮比较
                try:
                    if node[12] == node_compare[4]:
                        distance_ = [node[0], node_compare[0], int(node[12]), node[13],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[12] == node_compare[6]:
                        distance_ = [node[0], node_compare[0], int(node[12]), node[13],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[12] == node_compare[8]:
                        distance_ = [node[0], node_compare[0], int(node[12]), node[13],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[12] == node_compare[10]:
                        distance_ = [node[0], node_compare[0], int(node[12]), node[13],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[12] == node_compare[12]:
                        distance_ = [node[0], node_compare[0], int(node[12]), node[13],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[12] == node_compare[14]:
                        distance_ = [node[0], node_compare[0], int(node[12]), node[13],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)

                # 第六轮比较
                try:
                    if node[14] == node_compare[4]:
                        distance_ = [node[0], node_compare[0], int(node[14]), node[15],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[14] == node_compare[6]:
                        distance_ = [node[0], node_compare[0], int(node[14]), node[15],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[14] == node_compare[8]:
                        distance_ = [node[0], node_compare[0], int(node[14]), node[15],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[14] == node_compare[10]:
                        distance_ = [node[0], node_compare[0], int(node[14]), node[15],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[14] == node_compare[12]:
                        distance_ = [node[0], node_compare[0], int(node[14]), node[15],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)
                try:
                    if node[14] == node_compare[14]:
                        distance_ = [node[0], node_compare[0], int(node[14]), node[15],
                                     tools.geodistance(node[1], node[2], node_compare[1], node_compare[2])]
                        distance.append(distance_)
                except Exception as ex:
                    print(ex)

    # 路口按照way_id归类
    re = []
    way_id = []
    for ele in distance:
        if [ele[0], ele[3]] not in way_id:
            way_id.append([ele[0], ele[3]])

    for i in range(len(way_id)):
        re_ = []
        for ele in distance:
            if way_id[i] == [ele[0], ele[3]]:
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
    return distance, re, re_sort


def delete_same_node(distance, df):
    delete_node = []
    for ele in distance:
        if ele[4] == 0 and ele[0] < ele[1] and ele[1] not in delete_node:
            delete_node.append(ele[1])
    df_ = df
    for ele in delete_node:
        df_ = df_.drop(ele)
    return delete_node, df_


def get_relation(re_sort, public_node_info):
    relation = []
    for re_sort_ in re_sort:
        relation_ = []
        angle_1 = tools.getDegree(public_node_info[re_sort_[0][0]][1], public_node_info[re_sort_[0][0]][2],
                                  public_node_info[re_sort_[0][1]][1], public_node_info[re_sort_[0][1]][2])
        for re_sort_ele in re_sort_:
            angle_2 = tools.getDegree(public_node_info[re_sort_ele[0]][1], public_node_info[re_sort_ele[0]][2],
                                      public_node_info[re_sort_ele[1]][1], public_node_info[re_sort_ele[1]][2])
            if abs(angle_1 - angle_2) >= 90:
                relation_.append(re_sort_[0])
                relation_.append(re_sort_ele)
                relation.append(relation_)
                break
            try:
                if angle_2 == tools.getDegree(public_node_info[re_sort_ele[0]][1], public_node_info[re_sort_ele[0]][2],
                                              public_node_info[re_sort_[len(re_sort_) - 1][1]][1],
                                              public_node_info[re_sort_[len(re_sort_) - 1][1]][2]):
                    relation_.append(re_sort_[0])
                    relation.append(relation_)
                    break
            except Exception as ex:
                print(re_sort_[len(re_sort_) - 1][0])
                print(ex.args)
                print('=========')
                print(traceback.format_exc())
    return relation


def write_relation_to_csv(relation, public_node_info):
    # relation的index范围为0-1001
    relation_1001 = []
    for i in range(1002):
        same_node = []
        for relation_ in relation:
            if relation_[0][0] == i:
                for relation_ele in relation_:
                    same_node.append(relation_ele)
            if relation_[0][0] > i:
                break
        relation_1001.append(same_node)
    del(relation_1001[998])
    relation_file = []
    for single_relation in relation_1001:
        try:
            relation_file_ = [single_relation[0][0]]
        except Exception as ex:
            print(single_relation)
            print(ex.args)
            print('=========')
            print(traceback.format_exc())
        for ele in single_relation:
            # 添加target, way_id, way_name, distance, direction
            relation_file_.append(ele[1])
            relation_file_.append(ele[2])
            relation_file_.append(ele[3])
            relation_file_.append(ele[4])
            relation_file_.append(get_direction(public_node_info[ele[0]][1], public_node_info[ele[0]][2],
                                                public_node_info[ele[1]][1], public_node_info[ele[1]][2]))
        relation_file.append(relation_file_)
    df = pd.DataFrame(relation_file,
                      columns=[
                          'start_point',
                          'target_point_one', 'way_id_one', 'way_name_one', 'distance_one', 'direction_one',
                          'target_point_two', 'way_id_two', 'way_name_two', 'distance_two', 'direction_two',
                          'target_point_three', 'way_id_three', 'way_name_three', 'distance_three', 'direction_three',
                          'target_point_four', 'way_id_four', 'way_name_four', 'distance_four', 'direction_four',
                          'target_point_five', 'way_id_five', 'way_name_five', 'distance_five', 'direction_five',
                          'target_point_six', 'way_id_six', 'way_name_six', 'distance_six', 'direction_six'
                      ])
    df.to_csv('public_node_relation.csv', index=False, encoding="utf-8")
    return relation_file


if __name__ == '__main__':
    # 第一阶段
    # file_path = "public_node_info.csv"
    # df = pd.read_csv(file_path, encoding='utf-8')
    # di, re, re_sort = get_shortest_node_by_same_id(df.values.tolist())
    # de_no, df_1 = delete_same_node(di, df)
    # df_1 = df_1.reset_index(drop=True)
    # df_1 = df_1.drop(['Unnamed: 0'], axis=1)
    # df_1.to_csv('public_node_info_.csv', index=True, encoding="utf-8")

    # 第二阶段
    file_path_ = "public_node_info_.csv"
    df_ = pd.read_csv(file_path_, encoding='utf-8')
    di, re, re_sort = get_shortest_node_by_same_id(df_.values.tolist())
    relation = get_relation(re_sort, df_.values.tolist())
    relation_file = write_relation_to_csv(relation, df_.values.tolist())

    # df = df.fillna(-1)
