def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        return 0.0
    return sum(values) / len(values)
#Проверки arithmetic_mean
assert arithmetic_mean([1, 2, 3]) == 2.0
assert arithmetic_mean([10.0, 20.0]) == 15.0
assert arithmetic_mean([5]) == 5.0
print('Позиционный вызов')
print(arithmetic_mean([4, 8, 15]))
def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name:
        return ""
    parts = [part.capitalize() for part in name.split() if part]
    return " ".join(parts)
#Проверки normalize_name
assert normalize_name("  дарья   стрепеткова ") == "Дарья Стрепеткова"
assert normalize_name("ANNA MARIE") == "Anna Marie"
assert normalize_name("   ") == ""
print('Позиционный и именованный вызовы')
print(normalize_name("  иван   петров "))
print(normalize_name(name="  МАРИЯ   иванова "))
def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if not student or not results:
        return f"{prefix} для {student or 'неизвестного студента'} отсутствуют."
    average = arithmetic_mean(results)
    return (
        f"{prefix} студента {student}: "
        f"средний балл {average:.{precision}f} "
        f"по {len(results)} результатам."
    )
#Проверки build_report
assert build_report("Иван", [5, 4]) == ("Результат студента Иван: средний балл 4.50 по 2 результатам.")
assert build_report("Иван", [5, 4], precision=0) == ("Результат студента Иван: средний балл 4 по 2 результатам.")
assert build_report(student="Иван", results=[5, 4], prefix="Итог") == ("Итог студента Иван: средний балл 4.50 по 2 результатам.")
print('Позиционный вызов')
print(build_report("Иван", [5, 4]))
print('Именованный вызов')
print(build_report(student="Иван", results=[5, 4], prefix="Итог"))
def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    cleaned_tags = []
    for tag in tags:
        if not tag:
            continue
        cleaned_tag = tag.strip()
        if not cleaned_tag:
            continue
        if lowercase:
            cleaned_tag = cleaned_tag.lower()
        if cleaned_tag not in cleaned_tags:
            cleaned_tags.append(cleaned_tag)
    return tuple(cleaned_tags)
# Проверки collect_tags
assert collect_tags(" Python ", "python", "AI") == ("python", "ai")
assert collect_tags("Python", lowercase=False) == ("Python",)
assert collect_tags("", "  ", "Data") == ("data",)
print('Позиционный вызов')
print(collect_tags(" Python ", "AI", "python"))
print('Именованный вызов')
print(collect_tags("Python", "AI", lowercase=False))
# Демонстрация распаковки списка через * и словаря через **
scores = [85, 90, 78]
options = {
    "precision": 1,
    "prefix": "Итог",
}
report = build_report("Дарья Стрепеткова", scores, **options)
assert report == ("Итог студента Дарья Стрепеткова: средний балл 84.3 по 3 результатам.")
print(report)
print('Исследование LEGB')
course = "Python"
def demonstrate_legb() -> str:
    """Показывает LEGB и изменение переменной объемлющей функции через nonlocal."""
    topic = "области видимости"

    def inner() -> str:
        nonlocal topic
        topic = "LEGB и замыкания"
        return f"{course}: {topic}"

    return inner()
legb_result = demonstrate_legb()
assert legb_result == "Python: LEGB и замыкания"
assert course == "Python"
print(legb_result)
print('Ошибка изменяемого значения по умолчанию')
def add_result(value: int, results: list[int] | None = None) -> list[int]:
    """Добавляет результат в новый или переданный список без общего состояния."""
    if results is None:
        results = []
    results.append(value)
    return results
first_result = add_result(1)
second_result = add_result(2)
assert first_result == [1]
assert second_result == [2]
assert first_result is not second_result
print(first_result)
print(second_result)
print('Практическое расширение')
def apply_to_results(
    operation,
    values,
):
    """Применяет переданную функцию к каждому результату."""
    return [operation(value) for value in values]
def double(value: int) -> int:
    """Удваивает переданное значение."""
    return value * 2
doubled_results = apply_to_results(double, [1, 2, 3])
incremented_results = apply_to_results(lambda value: value + 1, [1, 2, 3])
assert doubled_results == [2, 4, 6]
assert incremented_results == [2, 3, 4]
print(doubled_results)
print(incremented_results)
def make_threshold_checker(threshold: int):
    """Создает функцию для проверки достижения порога."""
    def check(result: int) -> bool:
        return result >= threshold
    return check
passed_80 = make_threshold_checker(80)
passed_90 = make_threshold_checker(90)
assert passed_80(85) is True
assert passed_90(85) is False
assert passed_80(90) is True
assert passed_90(90) is True
print(passed_80(85))
print(passed_90(85))
