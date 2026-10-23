a = int(input('Результат студента: '))
b = input('Тип работы: ')
c = int(input('Количество пропущенных занятий: '))
# часть 1
if (0 > a or a > 100):
    print('Данные о результатах студента неккоректны')
elif (c < 0 or c > 5):
    print('Данные о посещении неккоректны')
else:  # часть 2
    if 90 <= a:
        lev = 'отличный'
    elif 75 <= a:
        lev = 'хороший'
    elif 60 <= a:
        lev = 'удовлетворительный'
    else:
        lev = 'недостаточный'
    if c > 3:
        if lev == 'отличный':
            lev = 'хороший'
        elif lev == 'хороший':
            lev = 'удовлетворительный'
        elif lev == 'удовлетворительный':
            lev = 'недостаточный'
    match b:   # часть 3
        case 'exam':
            work = 'экзаменационная работа'
        case 'project':
            work = 'проектная работа'
        case 'practice':
            work = 'практическая работа'
        case _:
            work = 'неизвестный тип работы'
    print(f'Результат: {a}')
    print(f'Тип работы: {work}')
    print(f'Пропуски: {c}')
    print(f'Уровень: {lev}')
# Практическое расширение
def f(score, work_type, absences):
    if score >= 90:
        level = "отличный"
    elif score >= 75:
        level = "хороший"
    elif score >= 60:
        level = "удовлетворительный"
    else:
        level = "недостаточный"

    if absences > 3:
        if level == "отличный":
            level = "хороший"
        elif level == "хороший":
            level = "удовлетворительный"
        elif level == "удовлетворительный":
            level = "недостаточный"

    match work_type:
        case "exam":
            work = "экзаменационная работа"
        case "project":
            work = "проектная работа"
        case "practice":
            work = "практическая работа"
        case _:
            work = "неизвестный тип работы"
    if score >= 90:
        level = "отличный"
    elif score >= 75:
        level = "хороший"
    elif score >= 60:
        level = "удовлетворительный"
    else:
        level = "недостаточный"

    if absences > 3:
        if level == "отличный":
            level = "хороший"
        elif level == "хороший":
            level = "удовлетворительный"
        elif level == "удовлетворительный":
            level = "недостаточный"

    match work_type:
        case "exam":
            work_description = "экзаменационная работа"
        case "project":
            work_description = "проектная работа"
        case "practice":
            work_description = "практическая работа"
        case _:
            work_description = "неизвестный тип работы"

    return (f"Результат: {score}; тип работы: {work_description}; пропуски: {absences}; уровень: {level}.")
student = [(95, 'exam', 0), (88, 'project', 2), (72, 'practice', 1), (58, 'exam', 0), (91, 'project', 4), (76, 'practice', 5), (63, 'exam', 4), (45, 'project', 0), (100, 'practice', 0), (67, 'exam', 2), (83, 'project', 3),]
lev_count = {
    'отличный': 0,
    'хороший': 0,
    'удовлетворительный': 0,
    'недостаточный': 0
}
for x in student:
    res = f(*x)
    print(res)
    for y in lev_count:
        if res.endswith(f'уровень: {y}.'):
            lev_count[y] += 1
            break
for x, y in lev_count.items():
    print(f'{x}: {y}')
