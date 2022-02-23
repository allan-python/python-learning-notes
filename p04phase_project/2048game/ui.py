"""
2. 界面视图模块
        创建游戏核心类对象
        调用核心类对象的生成数字方法
        while True:
            呈现界面
            获取用户输入，调用核心类对象的移动方法.
            产生随机数
    """
from bll import GameCoreController
from model import Direction
# import os


class GameConsoleView:
    def __init__(self):
        self.__control = GameCoreController()

    def __display_menu(self):
        """
            打印游戏列表
        """
        # 清空控制台
        # os.system("clear")
        __list_target = self.__control.map
        for r in range(len(__list_target)):
            for c in range(len(__list_target[r])):
                print(__list_target[r][c], end="\t")
            print()

    def __merge_map(self):
        """
            合并数字
        """
        result_dir = input("请输入合并方向（w s a d）：")
        if result_dir == "w":
            self.__control.move(Direction.up)
        if result_dir == "s":
            self.__control.move(Direction.down)
        if result_dir == "a":
            self.__control.move(Direction.lift)
        if result_dir == "d":
            self.__control.move(Direction.right)

    def start(self):
        """
            开始游戏
        """
        self.__control.generate_nuw_number()
        self.__display_menu()

    def update(self):
        """
            更新游戏
        """
        while True:
            self.__merge_map()
            # if 界面发生变化（具体实现放在bll里面定义）
            if self.__control.is_change:
                self.__control.generate_nuw_number()
                self.__display_menu()
            elif self.game_over():
                print("游戏结束")
                break

    def game_over(self):
        """
            结束游戏
        """
        return self.__control.is_game_over()

