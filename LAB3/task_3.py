submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]
students = set()
lab = set()
sl_pop = {}
sl_best_res = {}
sl_pop2 = {}
for st, labor, score in submissions:
    students.add(st)
    lab.add(labor)
    if st not in sl_pop:
        sl_pop[st] = []
    sl_pop[st].append(score)
    key = (st, labor)
    if (key not in sl_best_res) or (score > sl_best_res[key]):
        sl_best_res[key] = score
    sl_pop2[key] = sl_pop2.get(key, 0) + 1

def f(st, labor, score):
    students.add(st)
    lab.add(labor)
    if st not in sl_pop:
        sl_pop[st] = []
    sl_pop[st].append(score)
    key = (st, labor)
    if (key not in sl_best_res) or (score > sl_best_res[key]):
        sl_best_res[key] = score
    sl_pop2[key] = sl_pop2.get(key, 0) + 1
def f1():
    print('Студенты:', students)
    print('Лабораторные работы:', lab)
    print('Попытки студентов:', sl_pop)
    print('Лучшие результаты:', sl_best_res)
    print('Количество попыток:', sl_pop2)
    students_lab_01 = set()
    students_lab_02 = set()
    students_both_labs = set()
    for student, laboratory in sl_pop2:
        if laboratory == "lab_01":
            students_lab_01.add(student)
        elif laboratory == "lab_02":
            students_lab_02.add(student)
        students_both_labs = students_lab_01 & students_lab_02
    print("Студенты, сдавшие обе работы:", students_both_labs)
print('До изменений:')
f1()
print('После:')
f('daria', 'lab_02', 4)
f1()
#Практическое расширение
def f2(s):
    parts = s.strip().split()
    if not parts:
        print('Пустой запрос')
        return 1
    com = parts[0]
    if com == 'student' and len(parts) == 2:
        student = parts[1]
        if student in sl_pop:
            print(f'Попытки {student}: {sl_pop[student]}')
        else:
            print(f'Студент {student} не найден')
    elif com == 'best' and len(parts) == 3:
        student, laboratory = parts[1], parts[2]
        key = (student, laboratory)
        if key in sl_best_res:
            print(f"Лучший результат {student} по {laboratory}: {sl_best_res[key]}")
        else:
            print(f"Нет попыток {student} по {laboratory}")
    elif com == "attempts" and len(parts) == 3:
        student, laboratory = parts[1], parts[2]
        key = (student, laboratory)
        if key in sl_pop2:
            print(f"Попыток {student} по {laboratory}: {sl_pop2[key]}")
        else:
            print(f"Нет попыток {student} по {laboratory}")
    elif com == "completed" and len(parts) == 2:
        laboratory = parts[1]
        if laboratory in lab:
            students_for_lab = set()
            for student, lab1 in sl_pop2:
                if lab1 == laboratory:
                    students_for_lab.add(student)
            print(f"Сдавали {laboratory}: {students_for_lab}")
        else:
            print(f"Лабораторная работа {laboratory} не найдена")
    else:
        print("Неизвестная команда или неверный формат запроса")
print('Примеры запросов:')
f2('student anna')
f2('best anna lab_01')
f2('attempts boris lab_02')
f2('completed lab_01')
f2('completed lab_03')
f2('bad anna')

    
