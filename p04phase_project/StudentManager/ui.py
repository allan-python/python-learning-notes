"""
    ui 界面
        表示层
"""
from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    """
        学生界面视图类
    """
    def __init__(self):
        # 创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_student(self):
        """
            录入学生信息
        """
        # 1. 在控制台中录入学生信息，存成学生对象StudentModel
        # 2. 调用逻辑控制器的add_student方法
        stu = StudentModel()
        # try:
        #     stu.name = str(input("请输入姓名："))
        #     break
        # except:
        #     print("输入有误")
        # while True:
        #     try:
        #         stu.age = int(input("请输入年龄："))
        #         break
        #     except:
        #         print("输入有误")
        # while True:
        #     try:
        #         stu.score = float(input("请输入成绩："))
        #         break
        #     except:
        #         print("输入有误")
        stu.name = self.__get_str_error("请输入姓名：")
        stu.age = self.__get_int_error("请输入年龄：")  # int类型
        stu.score = self.__get_float_error("请输入成绩：")  # int类型
        self.__manager.add_student(stu)

    def __output_student(self, list_target):
        """
            显示录入的学生信息
        """
        for item in list_target:
            print("编号:", item.id, "姓名:", item.name, "年龄:", item.age, "成绩:", item.score)

    def __output_student_by_score(self):
        """
            学生按成绩由低-高显示学生信息
        """
        list_target = self.__manager.oder_by_score()
        self.__output_student(list_target)

    def __delete_student(self):
        """
            删除指定编号的学生
        :return:
        """
        # 删除指定姓名的学生
        # self.stu = str(input("请输入要删除的名字："))
        self.stu = self.__get_str_error("请输入要删除的名字")
        if self.__manager.remove_student(self.stu):
            print("删除成功")
        else:
            print("删除失败")

    @property
    def delete_student(self):
        return self.__delete_student

    def __modify_student(self):
        """
            修改学生信息
        :return:
        """
        stu = StudentModel()    # 用一个类包一下信息
        # stu.id = int(input("请输入要修改的学生编号"))
        # stu.name = input("请输入姓名")
        # stu.age = int(input("请输入年龄"))
        # stu.score = input("请输入成绩")
        stu.id = self.__get_int_error("请输入要修改的学生编号")
        stu.name = self.__get_str_error("请输入姓名")
        stu.age = self.__get_int_error("请输入年龄")
        stu.score = self.__get_float_error("请输入成绩")
        if self.__manager.update_student(stu):
            print("更新成功")
        else:
            print("更新失败")

    def __dispaly_menu(self):
        """
            显示菜单
        """
        print("1)  添加学生")
        print("2)  显示学生")
        print("3)  删除学生")
        print("4)  修改学生")
        print("5)  按学生成绩低—高显示学生")

    def __select_menu(self):
        """
            选择菜单
        """
        number = input("请输入选项：")
        if number == "1":    # 添加学生信息
            self.__input_student()
        elif number == "2":  # 显示学生信息
            self.__output_student(self.__manager.stu_list)
        elif number == "3":    # 删除学生信息
            self.__delete_student()
        elif number == "4":    # 修改学生信息
            self.__modify_student()
        elif number == "5":    # 学生按成绩由低-高排序
            self.__output_student_by_score()

    def __get_int_error(self, msg):
        while True:
            try:
                return int(input(msg))
            except Exception:
                print("输入有误")

    def __get_str_error(self, msg):
        while True:
            try:
                return str(input(msg))
            except:
                print("输入有误")

    def __get_float_error(self, msg):
        while True:
            try:
                return float(input(msg))
            except:
                print("输入有误")

    def main(self):
        """
        界面入口方法
        """
        while True:
            self.__dispaly_menu()
            self.__select_menu()

