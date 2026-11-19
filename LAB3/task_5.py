students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}
def mean(values):  #Средн ариф
    if not values:
        return 0.0

    return sum(values) / len(values)
def minimum(values):   #мин балл
    if not values:
        return None
    result = values[0]
    for value in values[1:]:
        if value < result:
            result = value
    return result
def maximum(values):   #макс балл
    if not values:
        return None
    result = values[0]
    for value in values[1:]:
        if value > result:
            result = value
    return result
def classify(score):     #оценка текстовая
    if score >= 90:
        return "отлично"
    if score >= 75:
        return "хорошо"
    if score >= 60:
        return "удовлетворительно"
    return "неудовлетворительно"
def student_summary(name, results):   #словарь со всеми итогами 1го студента
    average = mean(results)
    lowest = minimum(results)
    highest = maximum(results)
    return {
        "name": name,
        "results": results.copy(),
        "average": average,
        "minimum": lowest,
        "maximum": highest,
        "category": classify(average),
    }
def group_summary(students):     #статистика текстовых оценок
    summaries = []
    for name, results in students.items():
        summaries.append(student_summary(name, results))
    categories = {
        "отлично": 0,
        "хорошо": 0,
        "удовлетворительно": 0,
        "неудовлетворительно": 0,
    }
    for summary in summaries:
        categories[summary["category"]] += 1
    all_results = []
    for results in students.values():
        all_results.extend(results)
    return {
        "students": summaries,
        "categories": categories,
        "group_average": mean(all_results),
    }
def find_top_students(students):   #студент с макс ср результатом
    if not students:
        return []
    top_average = None
    top_students = []
    for name, results in students.items():
        average = mean(results)
        if top_average is None or average > top_average:
            top_average = average
            top_students = [name]
        elif average == top_average:
            top_students.append(name)
    return top_students
def format_report(student_data, group_data):    #общий итоговый отчет
    if not student_data:
        return "Группа пуста."
    lines = ["Отчет по учебным результатам", ""]
    for student in student_data:
        lines.append(f"Студент: {student['name']}")
        lines.append(f"Средний результат: {student['average']:.2f}")
        lines.append(f"Минимальный результат: {student['minimum']}")
        lines.append(f"Максимальный результат: {student['maximum']}")
        lines.append(f"Категория: {student['category']}")
        lines.append("")
    lines.append("Количество студентов по категориям:")
    for category, count in group_data["categories"].items():
        lines.append(f"{category}: {count}")
    lines.append("")
    lines.append(f"Общий средний результат группы: {group_data['group_average']:.2f}")
    top_students = find_top_students({
        student["name"]: student["results"]
        for student in student_data
    })
    if top_students:
        lines.append(f"Лидеры группы: {', '.join(top_students)}")
    return "\n".join(lines)
#пример 1
group_data = group_summary(students)
student_data = group_data["students"]
report = format_report(student_data, group_data)
print(report)
print()
#пример 2
students1 = {
    "Анна": [78, 91, 84, 88],
}
group_data1 = group_summary(students1)
student_data1 = group_data1["students"]
report1 = format_report(student_data1, group_data1)
print(report1)
print()
#пример 3
students2 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [90, 83, 68, 100],
    "Дарья": [50, 51],
}
group_data2 = group_summary(students2)
student_data2 = group_data2["students"]
report2 = format_report(student_data2, group_data2)
print(report2)
print()
#пример 4
students3 = {}
group_data3 = group_summary(students3)
student_data3 = group_data3["students"]
report3 = format_report(student_data3, group_data3)
print(report3)
print()
# Пример 5
students4 = {
    "Анна": [],
    "Борис": [90, 83, 68, 100],
    "Дарья": [50, 51],
}
group_data4 = group_summary(students4)
student_data4 = group_data4["students"]
report4 = format_report(student_data4, group_data4)
print(report4)
print()
# Пример 6
students5 = {
    "Анна": [0],
    "Борис": [100],
}
group_data5 = group_summary(students5)
student_data5 = group_data5["students"]
report5 = format_report(student_data5, group_data5)
print(report5)
print()
