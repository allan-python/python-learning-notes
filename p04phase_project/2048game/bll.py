"""
    逻辑处理模块
    1. 实现逻辑处理模块
        （1）创建游戏核心类 GameCoreController
        （2）将核心算法粘贴进来，将所有参数改为成员变量
        （3）产生新数字
            -- 计算所有空白位置（为0的位置）
            -- 随机选择一个位置
            -- 根据概率产生数字，存入列表的相应位置
"""
from model import Location, Direction
import random
import copy


class GameCoreController:
    """
        游戏核心控制器
    """
    def __init__(self):
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4
        ]
        # 测试游戏是否结束的数据
        # self.__map = [
        #     [2, 2, 8, 16],
        #     [4, 2, 23, 45],
        #     [3, 5, 9, 7],
        #     [15, 14, 12, 10]
        # ]
        # 用于存储去零和合并的列表
        self.__list_merge = []
        # 用于存储空位置的列表
        self.__list_empty_location = []
        # 判断地图是否发生变化
        self.is_change = False

    @property
    def map(self):
        return self.__map

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __zero_to_end(self):
        """
            将零元素移动到列表末尾
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)
        return self.__list_merge

    def __merge(self):
        """
            合并相同的非零元素
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0
                # self.__calculate_empty()
        self.__zero_to_end()
        return self.__list_merge

    def __move_lift(self):
        """
            按行向左合并相同元素
        """
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.__merge()
            self.__map[r][:] = self.__list_merge
        return self.__map

    def __move_right(self):
        """
            按行向右合并相同元素
        """
        for r in range(len(self.__map)):
            self.__list_merge = self.__map[r][::-1]
            self.__merge()
            self.__map[r][::-1] = self.__list_merge
        return self.__map

    def __move_up(self):
        """
            按行向上合并相同元素
        """
        for c in range(len(self.__map)):
            # 清空合并列表，目的：避免之前结果对本次有影响
            self.__list_merge.clear()
            for r in range(len(self.__map[c])):
                self.__list_merge.append(self.__map[r][c])
            self.__merge()
            for r in range(len(self.__map)):
                self.__map[r][c] = self.__list_merge[r]
        return self.__map

    def __move_down(self):
        """
            按行向上合并相同元素
        """
        for c in range(len(self.__map)):
            # 清空合并列表，目的：避免之前结果对本次有影响
            self.__list_merge.clear()
            for r in range(len(self.__map) - 1, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.__merge()
            for r in range(len(self.__map) - 1, -1, -1):
                self.__map[r][c] = self.__list_merge[len(self.__map) - 1 - r]
        return self.__map

    def __equal_map(self, original):
        for r in range(4):
            for c in range(4):
                if original[r][c] != self.__map[r][c]:  # 表示有变化
                    return True
        return False

    def __calculate_empty_location(self):
        """
            计算空白位置
        """
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    # 创建位置对象
                    loc = Location(r, c)
                    self.__list_empty_location.append(loc)

    def generate_nuw_number(self):
        """
            根据概率随机生成新数字
        """
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return False
        # 从空位置列表中，随机产生一个元素.
        loc = random.choice(self.__list_empty_location)
        # 随机生成数字   10%的概率取4 ，90%的概率取2
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        # 删除空列表中的已有元素位置
        self.__list_empty_location.remove(loc)

    def move(self, dir_num):
        """
            移动合集
            dir：Direction类型
        """
        # 假设没有发生变化
        self.is_change = False
        # 移动前记录地图
        original_map = copy.deepcopy(self.__map)     # 通过深拷贝（二维列表）记录移动前的地图
        # original_map = self.__map    # self.__map修改，original_map也会改变
        # original_map = self.__map.copy()    # 浅拷贝只是拷贝了列表中的地址，
        if dir_num == Direction.up:
            self.__move_up()
        elif dir_num == Direction.down:
            self.__move_down()
        elif dir_num == Direction.lift:
            self.__move_lift()
        elif dir_num == Direction.right:
            self.__move_right()
        # 移动后对比地图
        self.is_change = self.__equal_map(original_map)

    def is_game_over(self):
        """
            判断游戏是否游戏结束
        """
        # 1. 空位置长度大于0，游戏不结束
        if len(self.__list_empty_location) > 0:
            return False
        # # 2. 如果横向具有相同元素，游戏不结束
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map)-1):
        #         if self.__map[r][c] == self.__map[r][c+1]:
        #             return False
        # # 3. 如果竖向具有相同元素，游戏不结束
        # for c in range(len(self.__map)):
        #     for r in range(len(self.__map)-1):
        #         if self.__map[r][c] == self.__map[r+1][c]:
        #             return False
        # 2+3. 横向竖向同时比较，是否具有相同元素
        for r in range(len(self.__map)):
            for c in range(len(self.__map)-1):
                if self.__map[r][c] == self.__map[r][c+1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False
        return True  # 如果以上条件都不满足，则游戏结束


# --------------测试代码------------------
# if __name__ == "__main__":

    # result = GameCoreController()
    # result.generate_nuw_number()
    # result.generate_nuw_number()
    # print("------------按行向左合并相同元素-------------")
    # print_list(result.merge_lift())
    # print("------------按行向右合并相同元素-------------")
    # print_list(result.merge_right())
    # print("------------按行向上合并相同元素-------------")
    # print_list(result.merge_up())
    # print("------------按行向下合并相同元素-------------")
    # print_list(result.merge_down())
    # print_list(result.map)







