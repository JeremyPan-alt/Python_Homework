def modify_grade(dic_stu, name, grade):
    if name in dic_stu:
        dic_stu[name] = grade
        print("更新数据：" + name + ", 成绩:" + str(grade))
    if name not in dic_stu:
        dic_stu[name] = grade
        print("插入数据：" + name + ", 成绩:" + str(grade))
    return dic_stu


def query_stu(dic_stu, name):
    if name in dic_stu:
        return dic_stu[name]
    if name not in dic_stu:
        return "学生信息不在数据库中！"


def construct(dic_stu, name, grade):
    if name in dic_stu:
        print(f"学生{name}已存在。")
    else:
        dic_stu[name] = grade
        print(f"学生{name} 已被添加，成绩为{grade}。")


def save_students(students, filename):
    with open(filename, 'w') as file:
        for name, grade in students.items():
            file.write(f"{name},{grade}\n")


def load_students(filename):
    students = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, grade = line.strip().split(',')
                students[name] = int(grade)
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
    return students

# 示例操作
students = {}
construct(students, "Alice", 90)
construct(students, "Bob", 85)
construct(students, "Alice", 75)
construct(students, "Bob", 92)
modify_grade(students, "Bob", 80)

query_stu(students, "Alice")

# 保存学生信息到文件
save_students(students, "students.txt")

# 假设程序重启，从文件加载学生信息
students_loaded = load_students("students.txt")
for name, grade in students_loaded.items():
    print(f"加载的学生：{name}, 成绩：{grade}")
