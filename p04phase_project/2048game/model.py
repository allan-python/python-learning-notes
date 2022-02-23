"""
    数据模块类
"""


class Location:
    """
        位置类
    """
    def __init__(self, r, c):
        """
            创建二维列表
        """
        self.r_index = r
        self.c_index = c

    @property
    def r_index(self):
        return self.__r_index

    @r_index.setter
    def r_index(self, value):
        self.__r_index = value

    @property
    def c_index(self):
        return self.__c_index

    @c_index.setter
    def c_index(self, value):
        self.__c_index = value


# 扩展：枚举
class Direction:
    """
        方向
    """
    up = 0
    down = 1
    lift = 2
    right = 3



