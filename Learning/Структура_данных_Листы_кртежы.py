# LESSON 3
# my_list = [1, 2, 3]
# print(my_list)

# sentence = 'What a wonderful life!'
# my_list1 = sentence.split(' ')
# print(my_list1)
# my_list2 = list(sentence)
# print(my_list2)

# возвести в квадрат
# numbers = [1, 2, 3, 5, 6]
# for number in numbers:
#     print(number**2)

# обращение к индексам
# print(numbers[0])
# print(numbers[4])
# print(numbers[-1])

# =====================================   МЕТОДЫ  ==========================================

# ==============  .APPEND() - для добавления эл. в список
# ==============  .INSERT() - для добавления эл. в конкретное место в списке
# ==============  .INDEX()  - для получения индекса эл.
# ==============  .СLEAR()  - для очистки списка
# ==============  .REMOVE() - для удаления эл.списка
# ==============  .REVERSE()- чтобы развернуть список эл. в списке
# ==============  .COUNT()  - для подсчета кол-ва эл. в списке
# ==============  SUM()    - для сложения эл. списка
# ==============  MIN()    - показывает эл. с самым низким значением в списке
# ==============  MAX()    - эл. с самым высоким значение в списке

# numbers[0] = 10
# print(numbers)
# print(id(numbers))
numbers = [1, 2, 3, 5, 6, 4 , 10 ,9, 10]
# print(id(numbers))
# numbers2 = [15, 20, 35]
# numbers.append(numbers2)
# print(numbers2)
# print(id(numbers))

# numbers.extend(numbers2)
# print(numbers)

# работает и мутирует список на месте и ничего не возвращает - None
# numbers.sort()
# print(numbers)

# возвращает новый список, но при этом изначальный список не изменится
# print(sorted(numbers))

# # отсортировали
# numbers.sort()
# print(numbers)
# # развернули в обратном порядке
# numbers.reverse()
# print(numbers)
# или
# print(numbers[::-1])

# получить часть списка - с 1 по 4 эл.
# print(numbers[0: 4])

# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

# сколько раз повторяется 10
# print(numbers.count(10))

# кол-во эл в листе
# print(len(numbers))

# ====================  Генерация списков (List comprehension)  ========================
# Позволяет использовать сокращенный синтаксис при создании списка на основе из уже сущ-го списка

# num2 = []
# for x in numbers:
#     if x%2:
#         num2.append((x * x))
# print(num2)
# # или
# num3 = [x * x for x in numbers if x%2]
# print(num3)

# l2 = ['a', 2, 2.0, None, 'b']
# print(l2)

# num4 = numbers
# print(num4)
# print(id(num4))
# print(id(numbers))
#
# num5 = numbers.copy()
# print(num5)
# print(id(num5))

# ====================  КОРТЕЖИ (TUPLES) - не изменяемая структура данных  ========================

# my_tuple = (1, 'apple', None, 2.5)
# print(my_tuple)
# print(type(my_tuple))
#
# my_tuple1 = 1, 5, 6, 8
# print(my_tuple1)
#
# print(tuple(numbers))

# ====================  Методы работы с Кортежами  ========================

# == INDEX - для вывода индекса эл.
# == COUNT - для подсчета кол-ва эл. в кортеже
# == SUM   - складывает все эл.
# == MIN   - эл. с наименьшим значеним
# == MAX   - эл. с масимальным значение
# == LEN   - кол-во эл. кортежа

# Кортежи исп-ся в случаях, когда важно соблюдать целостность данных, н-р координаты, название штатов,
# месяц, год, дни недели
# Можно передавать в ф-ю произвольное кол-во аргументов - DEF FUNC(*ARGS)
# Символ * означает, что кортеж нужно распаковать  - print(*numbers)

# def func(*args):
#     for item in args:
#         yield item * item
#
# for i in func(1, 2, 3, 4):
#     print(i)

# ====================  СЛОВАРЬ (DICTIONARY)  ========================
# Хранит коллекцию эл., где каждый эл. имеет: {ключ, значение}

my_dict = {
    'name': 'Alex',
    'surname': 'Smith',
    'age': '30',
    'department': 'IT'
}
# print(my_dict)
# print(my_dict['name'])
# print(my_dict['age'])
#
my_dict['salary'] = 10000
# print(my_dict)

# ====================  Методы Dictionary  ========================

# == .KEYS() - для вывода ключей словаря
# == .ITEMS() - для создания кортежей с ключами и значениями
# == .GET()   - для получения значения по ключу
# == .CLEAR() - сочистить словарь
# == .COPY()  - скопировать весь словарь
# == MIN()    - получить ключ с наименьшим значеним
# == MAX()    - получить ключ с масимальным значение
# == LEN()    - получить длину
# == TYPE()   - узнать тип


# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# == POP - возвращает и удаляет
# print(my_dict.pop('salary'))
# print(my_dict)
# get здесь ищет и возвращает None
# print(my_dict.get('salary', 'Not found'))

# for item in my_dict.items():
#     print(*item)

# for key in my_dict:
#     print(key)

# my_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3
# }
# result = 0
# for key in my_dict:
#     result += my_dict[key]
#     print(result)


# ====================  МНОЖЕСТВА (SETS)  ========================
# Множества похожи на словарь, в котором значения отброшены, а оставлены только ключи,
# как и в словаре, ключи д.б. уникальными. Т.е. значения не должны повторяться
# используются в математических вычислениях

# ====================  Методы SETS  ========================

# == .LEN(S)         - число эл. в множестве (размер множества)
# ==  X IN S         - принадлежит ли Х множеству S
# == .SET.ADD()      - добавляет эл. в множество
# == .SET.REMOVE()   - удаляет эл. из множества. KEYERROR если такого эл. не сузествует
# == .SET.POP()      - удаляет 1й эл. из множества, т.к множества не упорядочены,
# нельзя точно сказать, какой эл. будет 1м
# == .SET.CLEAR()    - очистка множества
# == SET.ISSUBSET(OTHER) или SET <= OTHER     - все эл. set принадлежат other

# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 555}
# set3 = {1, 2, 5}
#
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set3.issubset(set1))
# print(set1.issubset(set2))
# print(set1.difference(set3))
# print(set2.difference(set1))
# print(set2.symmetric_difference(set3))
# print(set3.add(8))
# print(set3)




