from folium import plugins
import folium
import os

# 31.2329298    121.4822705
m = folium.Map([31.2329298, 121.4822705], zoom_start=10)


def get_way_node(way_ref, location_map):
    all_location = []
    for m in way_ref:
        location = []
        for n in m:
            if n in location_map:
                location.append(location_map[n])
        all_location.append(location)
    draw_line(all_location)

def draw_line(all_location):
    for location in all_location:
        route = folium.PolyLine(
            location,
            weight = 5,
            color = 'black',
            opacity = 1
        ).add_to(m)
    m.save(os.path.join(r''+os.path.dirname(os.getcwd()) + '/dataset/', 'Heatmap1.html'))
