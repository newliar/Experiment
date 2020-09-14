import cross
import folium
import tools
import os


def t_intersected():
    A = cross.Point(0, 0)
    B = cross.Point(1, 0)
    C = cross.Point(1, 0)
    D = cross.Point(2, 0)
    print(cross.is_intersected(A, B, C, D))
    print(cross.get_intersection(A, B, C, D))


def draw_node_by_name(coordinate_info):
    way_name = []
    for way in coordinate_info:
        if way[0][1] not in way_name:
            way_name.append(way[0][1])
    for name in way_name:
        m = folium.Map([31.2240060, 121.4639028], zoom_start=15)
        for way in coordinate_info:
            if way[0][1] != name:
                continue
            else:
                color = tools.get_random_color()
                for ele in way:
                    location = [ele[4], ele[3]]
                    folium.Marker(
                        # folium格式，【纬度，经度】
                        location=location,
                        fill_color=color,
                        radius=6
                    ).add_to(m)
        m.save(os.path.join(r'' + os.path.dirname(os.getcwd()) + '/dataset/route/', name+'_node.html'))


# if __name__ == '__main__':
#     # t_intersected()
