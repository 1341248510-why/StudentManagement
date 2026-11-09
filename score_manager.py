def calculate_total(chinese,math,english)
    return chinese+math+english
def calculate_average(chinese,math,english):
    return calculate_total(chinese,math,english)/3
def get_result(average):
    if average>=60:
        return '及格'
    else
        return '不及格'