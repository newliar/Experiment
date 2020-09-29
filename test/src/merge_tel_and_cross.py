import pandas as pd
import tools


def merge_two_dataset():
    pd_cross = pd.read_csv('public_node_info_.csv', encoding='utf-8')
    pd_tel = pd.read_csv('tel_location.csv', encoding='utf-8')

    cross_list = pd_cross.values.tolist()
    tel_list = pd_tel.values.tolist()
    cross_addition = []
    for cross in cross_list:
        cross_addition_ = []
        for tel in tel_list:
            distance = tools.geodistance(cross[1], cross[2], tel[1], tel[2])
            if distance < 300:
                cross_addition_.append(int(tel[0]))
        cross_addition.append(cross_addition_)
    ser = pd.Series(cross_addition, name='tel')
    result = pd.concat([pd_cross, ser], axis=1)
    return result


if __name__ == '__main__':
    cross_tel = merge_two_dataset()
    cross_tel.to_csv('public_node_info_.csv', encoding='utf-8')
