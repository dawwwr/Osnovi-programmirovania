import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

import weakref
class Record:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Record({self.name})"
# 1.Создаем реестр на основе слабых ссылок
registry = weakref.WeakValueDictionary()
# 2.Создаем сильные ссылки на два объекта
record1 = Record("Первый")
record2 = Record("Второй")
#3 сильную ссылку сохраняем во временную переменную
temp_record = Record("Третий (Временный)")
# 3.Регистрируем все три объекта в слабом словаре
registry["rec1"] = record1
registry["rec2"] = record2
registry["rec3"] = temp_record
print("Сильные ссылки:", record1, record2, temp_record)
print("Содержимое реестра:", list(registry.values()))
assert len(registry) == 3
# 4.Удаляем временную сильную ссылку на третий объект
del temp_record
print("Оставшиеся в реестре записи:", list(registry.values()))
assert "rec3" not in registry, "Ошибка: третий объект должен был удалиться!"
assert len(registry) == 2
# 5.Удаляем сильную ссылку на второй объект
del record2
#Повторяем проверку состава реестра
print("Оставшиеся в реестре записи:", list(registry.values()))
assert "rec2" not in registry, "Ошибка: второй объект должен был удалиться!"
assert len(registry) == 1
assert registry["rec1"].name == "Первый"


