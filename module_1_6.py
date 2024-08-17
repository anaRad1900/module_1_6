# Работа со словарями
# Создаем переменную my_dict и присваиваем ей словарь из нескольких пар ключ-значение
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}

# Выводим словарь на экран
print("Dict:", my_dict)

# Выводим одно значение по существующему ключу
existing_value = my_dict.get('Masha')
print("Existing value:", existing_value)

# Выводим значение по отсутствующему ключу без ошибки
not_existing_value = my_dict.get('Ivan', None)
print("Not existing value:", not_existing_value)

# Добавляем ещё две произвольные пары в словарь
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915

# Удаляем одну из пар по существующему ключу и выводим значение этой пары
deleted_value = my_dict.pop('Egor', None)
print("Deleted value:", deleted_value)

# Выводим измененный словарь
print("Modified dictionary:", my_dict)

# Работа с множествами
# Создаем переменную my_set и присваиваем ей множество из разных типов данных с повторяющимися значениями
my_set = {1, 'Яблоко', 42.314, 'Яблоко', 1}
# Выводим множество на экран
print("Set:", my_set)

# Добавляем 2 произвольных элемента в множество
my_set.add(13)
my_set.add((5, 6, 1.6))

# Удаляем один любой элемент из множества
my_set.discard(1)  # Используем discard для безопасного удаления

# Выводим измененное множество
print("Modified set:", my_set)
