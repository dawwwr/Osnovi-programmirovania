name = input('Имя иследователя: ')
exper = input('Название эксперимента: ')
zapusk = int(input('Количество выполненных запусков: '))
time = float(input('Длительность одного запуска: '))
real = float(input('Действительная часть: '))
image = float(input('Мнимая часть: '))

total_z_t_s = zapusk * time
total_min = total_z_t_s / 60
compl = complex(real, image)
compl_2 = real ** 2 + image ** 2
has_runs = bool(zapusk)

print('========================================')
print(f"ЭКСПЕРИМЕНТ: {exper}")
print(f'Исследователь: {name}')
print(f'Запуски: {zapusk}')
print(f'Общее время: {total_z_t_s:.2f} с {total_min:.2f} мин')
print(f'Коэффициент: {compl}')
print(f'Квадрат модуля: {compl_2:.2f}')
print(f'Есть выполненные запуски: {has_runs}')
print('========================================')

print(type(name))
print(type(exper))
print(type(zapusk))
print(type(time))
print(type(real))
print(type(image))
print(type(total_z_t_s))
print(type(total_min))
print(type(compl))
print(type(compl_2))
print(type(has_runs))
