import os
import json
from lxml import etree
import xmltodict
import configuration

# ****************************
# 提取OSM文件有用信息并转成json文件
# ****************************

os.chdir(os.path.dirname(os.getcwd()) + "/dataset/")
osmfile = configuration.CITY+'_map.osm'


def iter_element(file_parsed, file_length, file_write):
    current_line = 0
    for event, element in file_parsed:
        current_line += 1
        elem_data = etree.tostring(element)
        elem_dict = xmltodict.parse(elem_data, attr_prefix="", cdata_key="")
        # # 存储node标签
        # if (element.tag == "node"):
        #     elem_jsonStr = json.dumps(elem_dict["node"])
        #     file_write.write(elem_jsonStr + "\n")
        # 存储way标签
        if element.tag == "way":
            elem_jsonStr = json.dumps(elem_dict["way"])
            file_write.write(elem_jsonStr + "\n")

        # 每次读取之后进行一次清空
        element.clear()
        while element.getprevious() is not None:
            del element.getparent()[0]


file_length = -1
for file_length, line in enumerate(open(osmfile, 'rU', encoding='utf-8')):
    pass
file_length += 1
print("length of the file:\t" + str(file_length))

file_node = open(configuration.CITY+"_ways.json", "w+")
file_parsed = etree.iterparse(osmfile, tag=["node", "way"])
iter_element(file_parsed, file_length, file_node)
file_node.close()
