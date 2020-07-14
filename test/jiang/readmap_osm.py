"""方法一"""
import os
import json
from lxml import etree
import xmltodict

os.chdir('C:\\Users\\Liar\\OneDrive\\科研')
osmfile = 'map.osm'
def iter_element(file_parsed, file_length, file_write):
    current_line = 0
    # try:
    for event, element in file_parsed:
        current_line += 1
        # print (current_line/float(file_length))
        elem_data = etree.tostring(element)
        elem_dict = xmltodict.parse(elem_data, attr_prefix="", cdata_key="")
        # print(element.tag)
        # if (element.tag == "node"):
        #     elem_jsonStr = json.dumps(elem_dict["node"])
        #     file_write.write(elem_jsonStr + "\n")
        if (element.tag == "way"):
            elem_jsonStr = json.dumps(elem_dict["way"])
            file_write.write(elem_jsonStr + "\n")
            # print("way")

        # 每次读取之后进行一次清空
        element.clear()
        while element.getprevious() is not None:
            del element.getparent()[0]
    # except:
    #     print("error")
    #     pass

file_length = -1
for file_length, line in enumerate(open(osmfile, 'rU',encoding = 'utf-8')):
    pass
file_length += 1
print( "length of the file:\t" + str(file_length))

file_node = open(osmfile+"way.json","w+")
file_parsed = etree.iterparse(osmfile, tag=["node","way"])
iter_element(file_parsed, file_length, file_node)
file_node.close()


# osm_json_file = 'F:\\数据集\\map1.osm_node.json'
# list1 = []
# with  open(osm_json_file,encoding = 'utf-8') as f:
#     for data in f:
#         tulist  = []
#         data= json.loads(data)
#         lat = float(data['lat'])
#         tulist.append(lat)
#         lon = float(data['lon'])
#         tulist.append(lon)
#         list1.append(tuple(tulist))
#
# source = list1
# from collections import defaultdict
# from collections import Counter
# Counter(list1)
# i = 0
# for k,v in Counter(list1).items():
#     if v == 2:
#         i += 1
#         print(k,v)
# print(i)



"""方法二"""
# import json
# import xml.dom.minidom
#
# dom = xml.dom.minidom.parse('map.osm')
# root = dom.documentElement
# nodelist = root.getElementsByTagName('node')
# waylist = root.getElementsByTagName('way')
#
# node_dic = {}
#
# #统计记录所有node
# for node in nodelist:
#     node_id = node.getAttribute('id')
#     node_lat = float(node.getAttribute('lat'))
#     node_lon = float(node.getAttribute('lon'))
#     node_dic[node_id] = (node_lat, node_lon)
#
# print (len(node_dic))
#
# #排除非路node
# for way in waylist:
#     taglist = way.getElementsByTagName('tag')
#     road_flag = False
#     for tag in taglist:
#         if tag.getAttribute('k') == 'highway':
#             road_flag = True
#     if not road_flag:
#         ndlist = way.getElementsByTagName('nd')
#         for nd in ndlist:
#             nd_id = nd.getAttribute('ref')
#             if nd_id in node_dic:
#                 node_dic.pop(nd_id)
#
# #print len(node_dic)
#
#
# with open('map.json', 'w') as fout:
#     json.dump(node_dic, fout)
