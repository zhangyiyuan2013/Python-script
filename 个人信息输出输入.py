students = []
while True:
    input_s = input('输入学生信息（学号 姓名 性别），空格分隔（输入q，则退出）：')

    if input_s == 'q':
        break

    input_cols = input_s.split(' ')
    students.append((input_cols[0], input_cols[1], input_cols[2]))

print(students)
