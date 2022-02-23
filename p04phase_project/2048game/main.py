"""
    游戏入口
"""
from ui import GameConsoleView

if __name__ == "__main__":
    view = GameConsoleView()
    view.start()         # 开始游戏
    view.update()        # 游戏更新
    view.game_over()     # 游戏结束
