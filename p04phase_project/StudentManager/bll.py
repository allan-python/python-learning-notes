"""
    bll 业务逻辑层
"""


class StudentManagerController:
    """
        学生逻辑控制类
    """
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加新学生
        :param stu: 需要添加的新学生对象
        """
        stu.id = self.__generate_id()
        self.__stu_list.append(stu)

    def __generate_id(self):
        """
            自动编号生成
        :return: 返回编号
        """
        # 生成编号的需求：新编号比上次添加的编号多1.
        # if len(self.__stu_list) > 0:
        #     id = self.__stu_list[-1].id + 1
        # else:
        #     id = 1
        # return id
        return self.__stu_list[-1].id + 1 if len(self.__stu_list) > 0 else 1

    def remove_student(self, stu):
        """
            删除指定编号的学生
        :param stu: 需输入的学生名字
        :return:
        """
        # 根据姓名删除指定学生
        for item in self.stu_list:
            if item.name == stu:
                self.stu_list.remove(item)
                return True
            return False

    def oder_by_score(self):
        """
            按成绩排序
        :return:
        """
        # 创建新列表，目的不影响原有列表
        list_target = self.stu_list[:]
        for r in range(len(list_target)-1):
            for c in range(r+1, len(list_target)):
                if list_target[r].score > list_target[c].score:
                    list_target[r], list_target[c] = list_target[c], list_target[r]
        return list_target

    def update_student(self, stu):
        """
            修改学生信息
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
            return False

