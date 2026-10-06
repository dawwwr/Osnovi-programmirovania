a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))
# Переназначение second
second = [10, 20, 30]

# Сравнение
print(first == second)    # True 
print(first is second)    # False 
# Изменение нового списка
second.append(40)

print(first, second)      # [10, 20, 30] [10, 20, 30, 40]
# first не изменился!
#Практическая задача
# создаем первую конфигурацию
config1 = {
    'Имя:': 'Проект Burmalda', 
    'Имена участников:': ['Даша', 'Маша'], 
    'Параметры запуска:': ['lr=0.01', 'b_size=32']
}
#Копия обычным присваиванием
config2 = config1
print(config1)
print(config2)
config2['Имена участников:'].append('Саша')
print(config1)
print(config2)
print(config1['Имена участников:'] is config2['Имена участников:'])
print(config1 is config2)

# независимое копирование
import copy
config3 = copy.deepcopy(config1)
print(config1)
print(config3)
config3['Имена участников:'].append('Петя')
print(config1)
print(config3)
print(config1['Имена участников:'] is config3['Имена участников:'])
print(config1 is config3)

assert 'Петя' not in config1['Имена участников:']
assert 'Петя' in config3['Имена участников:']
