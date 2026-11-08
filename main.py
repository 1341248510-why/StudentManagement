from student_manager import add_student,delete_student,update_student,search_student,load_students,save_students

students_dict=load_students()

while True:
    print('============学生管理系统===========')
    print('1.查询学生')
    print('2.删除学生')
    print('3.添加学生')
    print('4.修改学生成绩')
    print('5.退出系统')
    choice=input('请输入你的选择')
    if choice =='1':
        student_id=input('请输入你要查询的学号')
        search_student(students_dict,student_id)
    elif choice=='2':
        delete_student(students_dict)
        save_students(students_dict)
    elif choice=='3':
        add_student(students_dict)
        save_students(students_dict)
    elif choice=='4':
        update_student(students_dict)
        save_students(students_dict)
    elif choice=='5':
        print('结束，成功退出系统')
        break
    else:
        print('输入错误，没有这个选项，请重新输入:')