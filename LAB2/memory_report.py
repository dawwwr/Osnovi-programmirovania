import sys
import tracemalloc
results = []
# Размер отдельных объектов
objects = [
    ("Пустой список", [], 0),
    ("Список из 10 чисел", list(range(10)), 10),
    ("Кортеж из 10 чисел", tuple(range(10)), 10),
    ("Строка из 10 символов", "0123456789", 10),
    ("Целое число", 100, 1),
    ("None", None, 1)]
for name, obj, count in objects:
    results.append({
        "name": name,
        "count": count,
        "size": sys.getsizeof(obj),
        "current": 0,
        "peak": 0
    })
# Рост списка
numbers = []
old_size = sys.getsizeof(numbers)
for i in range(100):
    numbers.append(i)
    new_size = sys.getsizeof(numbers)
    if new_size != old_size:
        results.append({
            "name": "Рост списка",
            "count": len(numbers),
            "size": new_size,
            "current": 0,
            "peak": 0
        })
        old_size = new_size
# Список из 100000 чисел
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "list(range(100000))",
    "count": len(numbers),
    "size": sys.getsizeof(numbers),
    "current": current,
    "peak": peak
})
del numbers
# Объект range из 100000 чисел
tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
results.append({
    "name": "range(100000)",
    "count": len(numbers),
    "size": sys.getsizeof(numbers),
    "current": current,
    "peak": peak
})
# Единый отчёт
for result in results:
    print("Сценарий:", result["name"])
    print("Количество элементов:", result["count"])
    print("Размер внешнего объекта:", result["size"], "байт")
    print("Текущая память:", round(result["current"] / 1024, 2), "КБ")
    print("Пиковая память:", round(result["peak"] / 1024, 2), "КБ\n")
# Сравнение пиковой памяти
list_peak = results[-2]["peak"]
range_peak = results[-1]["peak"]
if range_peak > 0:
    print("Отношение пиковой памяти list/range:",
          round(list_peak / range_peak, 2))
