import json
import os

def getroad():
    file_path = os.path.dirname(os.getcwd())+"\\dataset\\allways.json"
    file = open(file_path, 'r', encoding='utf-8')
    # 存放 干线公路、一级道路、二级道路、三级道路
    trunk = []
    primary = []
    secondary = []
    tertiary = []
    # 存放道路连接路
    trunk_link = []
    primary_link = []
    secondary_link = []
    tertiary_link = []
    # 道路的ref
    trunk_ref = []
    trunk_link_ref = []

    #  将道路存放到对应的list
    for line in file.readlines():
        dic = json.loads(line)
        if "tag" in dic:
            if isinstance(dic["tag"], list):
                for m in dic["tag"]:
                    if m["v"] == "trunk":
                        trunk.append(dic)
                        break
                    if m["v"] == "primary":
                        primary.append(dic)
                        break
                    if m["v"] == "secondary":
                        secondary.append(dic)
                        break
                    if m["v"] == "tertiary":
                        tertiary.append(dic)
                        break
                    if m["v"] == "trunk_link":
                        trunk_link.append(dic)
                        break
                    if m["v"] == "primary_link":
                        primary_link.append(dic)
                        break
                    if m["v"] == "secondary_link":
                        secondary_link.append(dic)
                        break
                    if m["v"] == "tertiary_link":
                        tertiary_link.append(dic)
                        break
            elif dic["tag"]["v"] == "trunk":
                trunk.append(dic)
            elif dic["tag"]["v"] == "primary":
                primary.append(dic)
            elif dic["tag"]["v"] == "secondary":
                secondary.append(dic)
            elif dic["tag"]["v"] == "tertiary":
                tertiary.append(dic)
            elif dic["tag"]["v"] == "trunk_link":
                trunk_link.append(dic)
            elif dic["tag"]["v"] == "primary_link":
                primary_link.append(dic)
            elif dic["tag"]["v"] == "secondary_link":
                secondary_link.append(dic)
            elif dic["tag"]["v"] == "tertiary_link":
                tertiary_link.append(dic)


    print(get_way_ref(trunk_link, trunk_link_ref))

# 获得道路的所有ref值
def get_way_ref(way, way_ref):
    for ele in way:
        temp = []
        for nd_ele in ele["nd"]:
            for value in nd_ele.values():
                temp.append(value)
        way_ref.append(temp)
    return way_ref

if __name__ == "__main__":
    getroad()