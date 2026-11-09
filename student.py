class Student:
    def __init__(self,name,student_id,chinese,math,english):
        self.name=name
        self.student_id=student_id
        self.chinese=chinese
        self.math = math
        self.english= english

    def get_total_score(self):
        return sum([self.chinese, self.math, self.english])
    def get_result(self):
        if self.get_total_score()/3>=60:
            return'及格'
        else:
            return'不及格'

# 这是我的第一个Git版本管理练习
