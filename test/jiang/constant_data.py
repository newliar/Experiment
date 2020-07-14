USER_NUM = 511

MULTIPLE = 111000  # 对原坐标乘以的倍数

FILENUMBER = 100 # 100  # 每个行人读取的文件个数

ISDISPLAY = 1 # 获取道路json文件信息时是否可视化

ISDISPLAYTRAJECTORY = 0 # 1表示显示轨迹路径

ISDISPLAYSERVER = 1 # 1表示显示服务器

ISDISPLAYONETRAJECTORY = 0 # 表示显示某一条轨迹

USERNUMOFTRA = [50,51,52] # 表示显示路径的用户编号

OSMFILE = 'map1.osm'

# MAPPATH = "F:\数据集\mappku.osm_node.json" # 路网数据路径
MAPPATH = "C:/Users/Liar/OneDrive/科研/NSGA3/map.osm_way.json"

MATCHVALUE = 0.6 # 位置点匹配道路时距离参数所占比例

ISMATCHMAP = 80 # 当前用户不再匹配道路的阈值

ALLTIME = 900 # 实验时间总长，单位：秒

CAPCITYMULTIPLE = 0.5 # 服务器容量负载（50%，100%，150%）

CHOOSENUSERNUM = 512 # 选择的用户数量

# LAT = [39.975,40.005] # 清华经纬度
#
# LON = [116.28,116.36]

# LAT = [39.976,40.002]
#
# LON = [116.295,116.322]
#
# USERLAT = [39.976,40.002]
# USERLON = [116.295,116.322]

LAT = [] # 北大经纬度

LON = [116.30,116.327]

USERLAT = [39.976,40.00]
USERLON = [116.30,116.327]