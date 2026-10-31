measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
minn = 100
maxx = 0
summ = 0
chet_count = 0
arif = 0
for x in measurements:
    if x < minn:
        minn = x
    if x > maxx:
        maxx = x
    summ += x
    if x % 2 == 0:
        chet_count += 1
arif_chislo = summ / len(measurements)
for x in measurements:
    if x > arif_chislo:
        arif += 1
print('Сумма:', summ)
print('Минимальное значение:', minn)
print('Максимальное значение:', maxx)
print('Количество чётных значений:', chet_count)
print('Числа превосходящие ср. ариф.:', arif)
a = int(input('Введите число: '))
ind = -1
for i in range(len(measurements)):
    if measurements[i] == a:
        ind = i
        break
if ind == -1:
    print(f'Число {a} отсутствует в списке')
else:
    print(f'Первое вхождение числа {a} в списке под индексом {ind}')

#Дпоролнительный алгоритмический эксперимент
number = int(input('Введите положительное целое число для проверки простоты: '))
def f(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s = 3
    while s <= n ** 0.5:
        if n % s  == 0:
            return False
        s += 2
    return True
if f(number):
    print(f'Число {number} является простым')
else:
    print(f'Число {number} не является простым')

#Практическое расширение
import time
def liner_search(a1, x):
    comp = 0
    for i in range(len(a1)):
        comp += 1
        if a1[i] == x:
            return i, comp
    return -1, comp
def binari_search(a1, x):
    comp = 0
    lef = 0
    rig = len(a1) - 1
    while lef <= rig:
        mid = (lef + rig) // 2
        comp += 1
        if a1[mid] == x:
            return mid, comp
        comp += 1
        if a1[mid] < x:
            lef = mid + 1
        else:
            rig = mid - 1
    return -1, comp
a10 = [i for i in range(1, 11)]
a100 = [i for i in range(1, 101)]
a1000 = [i for i in range(1, 1001)]

print('Линейный поиск для 10 элементов:')
start = time.perf_counter()
lin10, comp10 = liner_search(a10, 10)
end = time.perf_counter()
print (f'Время выполнения: {(end - start):.6f} сек')
print('Колличество сравнений:', comp10)

print('Линейный поиск для 100 элементов:')
start = time.perf_counter()
lin100, comp100 = liner_search(a100, 100)
end = time.perf_counter()
print (f'Время выполнения: {(end - start):.6f} сек')
print('Колличество сравнений:', comp100)

print('Линейный поиск для 1000 элементов:')
start = time.perf_counter()
lin1000, comp1000 = liner_search(a1000, 1000)
end = time.perf_counter()
print (f'Время выполнения: {(end - start):.6f} сек')
print('Колличество сравнений:', comp1000)

print('Бинарный поиск для 10 элементов:')
start = time.perf_counter()
bin10, com10 = binari_search(a10, 10)
end = time.perf_counter()
print (f'Время выполнения: {(end - start):.6f} сек')
print('Колличество сравнений:', com10)

print('Бинарный поиск для 100 элементов:')
start = time.perf_counter()
bin100, com100 = binari_search(a100, 100)
end = time.perf_counter()
print (f'Время выполнения: {(end - start):.6f} сек')
print('Колличество сравнений:', com100)

print('Бинарный поиск для 10000 элементов:')
start = time.perf_counter()
bin1000, com1000 = binari_search(a1000, 1000)
end = time.perf_counter()
print (f'Время выполнения: {(end - start):.6f} сек')
print('Колличество сравнений:', com1000)

