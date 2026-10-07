import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
# состояние автоматического сборщика мусора
is_enabled = gc.isenabled()
print(is_enabled)
# пороги поколений
thresholds = gc.get_threshold()
print(thresholds)
# статистика поколений
stats = gc.get_stats()
print(stats)

#id()
print(id(first))
print(id(second))

# Удаляем first и second
del first
del second

# запускаем gc.collect()
collected = gc.collect()
print('Собрано объектов:', collected)

# Отключаем автоматический сборщик
gc.disable()
print('Автоматический выключен:', gc.isenabled)

#создаём 3 цикличиские структуры
a = []
b = []
c = []

a.append(b)
b.append(a)
b.append(c)
c.append(b)
print(a)
print(b)
print(c)
# удаляем внешние ссылки
del a
del b
del c
#запускаем ручную сборку
collect = gc.collect()
print('Собрано объектов:', collect)

# восстанавливаем автоматическую сборку
gc.enable()
print('Сборщик включен:', gc.isenabled())


#практическая задача
before = gc.collect()
print("Собрано до создания графа:", before)
# Три узла образуют цикл
n1 = {"name": "N1", "next": None}
n2 = {"name": "N2", "next": None}
n3 = {"name": "N3", "next": None}

# Независимый узел
n4 = {"name": "Node 4", "next": None}

# Связываем три узла в цикл
n1["next"] = n2
n2["next"] = n3
n3["next"] = n1

print(n1["next"]["name"])
print(n2["next"]["name"])
print(n3["next"]["name"])
print(n4["next"])

# Удаляем внешние ссылки на циклические узлы
del n1
del n2
del n3

# Ручная сборка
after = gc.collect()

print("Собрано после удаления графа:", after)

# Независимый узел всё ещё доступен
print("Независимый узел:", n4["name"])

