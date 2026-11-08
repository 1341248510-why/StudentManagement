from student import Student
import json

def add_student(students_dict):
    student_id=input('请输入学号:')
    while student_id in students_dict:
        print('该学生已存在，请重新输入')
        student_id=input()
    name=input('请输入姓名:')
    chinese=int(input('请输入语文成绩:'))
    math=int(input('请输入数学成绩:'))
    english=int(input('请输入英语成绩:'))
    new_student=Student(name,student_id, chinese,math,english)
    students_dict[student_id]=new_student

def delete_student(students_dict):
    student_id=input('请输入要删除的学号')
    if student_id in students_dict:
        del students_dict[student_id]
        print('删除成功')
    else:
        print('未找到该学生')

def update_student(students_dict):
    student_id=input('请输入要修改学生的学号')
    if student_id in students_dict:
        result = students_dict[student_id]
        result.chinese=int(input('请输入修改后的语文成绩'))
        result.math = int(input('请输入修改后的数学成绩'))
        result.english = int(input('请输入修改后的英语成绩'))
        print('修改成功')
    else:
        print('未找到该学生')

def search_student(students_dict,student_id):
    if student_id in students_dict:
        result=students_dict[student_id]
        print('姓名',result.name,'语文',result.chinese,'数学',result.math,'英语',result.english,'总分',result.get_total_score())
        print('考试结果:',result.get_result())
    else:
        print('未找到')

def load_students():
    students_dict={}
    try:
        with open('student.json','r',encoding='utf-8') as file:
            student_data = json.load(file)
            for key, value in student_data.items():
                 student = Student(value['name'], value['student_id'], value['chinese'], value['math'], value['english'])
                 students_dict[key] = student
    except FileNotFoundError:
        print('学生数据文件不存在，将使用空字典')
    return students_dict

def save_students(students_dict):
    students_data={}

    for key,value in students_dict.items():
        students_data[key]=value.__dict__
    with open('student.json', 'w', encoding='utf-8') as file:
        json.dump(students_data,file)
