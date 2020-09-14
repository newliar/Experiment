import os
import json
import configuration
import folium


def get_cr():
    file_path = os.path.dirname(os.getcwd()) + "\\dataset\\"+configuration.CITY+"_node.json"
    file = open(file_path, 'r', encoding='utf-8')
    cross = []
    for line in file.readlines():
        dic = json.loads(line)
        if "tag" in dic:
            if isinstance(dic["tag"], list):
                for ele in dic["tag"]:
                    if ele["v"] == "crossing":
                        cross.append(dic)
            elif dic["tag"]["v"] == "crossing":
                cross.append(dic)
    return cross


def draw_cross(crossing):
    location = []
    m = folium.Map([31.2240060, 121.4639028], zoom_start=15)
    for ele in crossing:
        location.append([ele['lat'], ele['lon']])
    for coordinate in location:
        folium.Marker(
            location=coordinate,
            fill_color='＃43d9de',
            radius=8
        ).add_to(m)
    m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/', 'cross_node.html'))


if __name__ == "__main__":
    crossing = get_cr()
    draw_cross(crossing)
