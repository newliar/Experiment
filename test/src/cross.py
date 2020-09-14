import numpy as np
import configuration as conf

f = 1000000
# 判断两线段是否相交
# https://segmentfault.com/a/1190000004457595?ref=myread


class Point(object):

    def __init__(self, x, y):
        self.x, self.y = x, y


# 向量
class Vector(object):

    def __init__(self, start_point, end_point):
        self.start_point, self.end_point = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y


ZERO = 1e-9


def negative(vector):
    """取反"""
    return Vector(vector.end_point, vector.start_point)


def vector_product(vectorA, vectorB):
    '''计算 x_1 * y_2 - x_2 * y_1'''
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y


def is_intersected(A, B, C, D):
    '''A, B, C, D 为 Point 类型'''
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    CA = negative(AC)
    CB = negative(BC)
    DA = negative(AD)
    DB = negative(BD)

    return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) \
        and (vector_product(CA, CB) * vector_product(DA, DB) <= ZERO)


# 求交点 联立方程组求点，线性代数解法
def get_intersection(A, B, C, D):
    # 求斜率
    # 考虑斜率不存在的情况
    if B.x-A.x == 0:
        k2 = (D.y-C.y)/(D.x-C.x)
        X = np.array([[1, 0], [k2, -1]])
        Y = np.array([A.x, k2*C.x-C.y])
    elif D.x - C.x == 0:
        k1 = (B.y-A.y)/(B.x-A.x)
        X = np.array([[k1, -1], [1, 0]])
        Y = np.array([k1*A.x-A.y, C.x])
    else:
        k1 = (B.y - A.y) / (B.x - A.x)
        k2 = (D.y - C.y) / (D.x - C.x)
        X = np.array([[k1, -1], [k2, -1]])
        Y = np.array([k1*A.x-A.y, k2*C.x-C.y])

    # 方程组的解
    try:
        XY = np.linalg.solve(X, Y)/conf.FACTOR
    except:
        print("**********************")
        print("矩阵不可逆")
        print("**********************")

    else:
        print(XY)
        return XY
