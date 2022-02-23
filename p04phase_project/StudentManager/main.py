"""
    程序入口
        注：代码越少越好
"""
import sys
print(sys.path)
import InstructionsTest
from ui import StudentManagerView


# 从当前模块运行.
if __name__ == "__main__":
    print(InstructionsTest.__doc__)
    view = StudentManagerView()
    view.main()
