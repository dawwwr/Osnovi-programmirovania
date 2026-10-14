import sys
import tracemalloc
# Часть 1. Размер отдельных объектов
a = []
b = list(range(10))
c = tuple(range(10))
d = "0123456789"
e = 10
f = None
print("Пустой список:", sys.getsizeof(a), 'б')
print("Список из 10 чисел:", sys.getsizeof(b), 'б')
print("Кортеж из 10 чисел:", sys.getsizeof(c), 'б')
print("Строка из 10 символов:", sys.getsizeof(d), 'б')
print("Целое число:", sys.getsizeof(e), 'б')
print("None:", sys.getsizeof(f), 'б')
# Часть 2. Рост списка
llist = []
size = sys.getsizeof(llist)
print("Длина:", len(llist), "Размер:", size)
for i in range(100):
    llist.append(i)
    new_size = sys.getsizeof(llist)
    if new_size != size:
        print("Длина:", len(llist), "Размер:", new_size, 'б')
        size = new_size
# Часть 3. Измерение через tracemalloc
tracemalloc.start()
numbers = list(range(100_000))
verna, pik = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Текущая память для списка:", verna / 1024, 'КБ')
print("Пиковая память для списка:", pik / 1024, 'КБ')
tracemalloc.start()
numbers = range(100_000)
verna, pik = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Текущая память для набора чисел:", verna / 1024, 'КБ')
print("Пиковая память для набора чисел:", pik / 1024, 'КБ')


