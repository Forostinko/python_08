# LESSON 2
#                            # ========   f-строки    ==========
#
# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name} Мне {age} лет.")
# # Меня зовут Дмитрий. Мне 25 лет.
#
# # поддерживают базовые арифметические операции
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")
# # 10 x 5 / 2 = 25.0
#
# # Позволяют обращаться к значениям списков по индексу
# planets = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f"Мы живим не планете {planets[2]}")
# # Мы живим не планете Земля
#
# # к элементам словаря по ключу
# planet = {"name": "Земля", "radius": 6378000}
# print(f"Планета {planet['name']}. Радиус {planet['radius']/1000} км.")
# # Планета Земля. Радиус 6378.0 км.
#
# # можете вызывать в f-строках методы объектов:
# name = "Дмитрий"
# print(f"Имя: {name.upper()}")
# # Имя: ДМИТИРИЙ
#
# # также вызывать функции:
# print(f"13 / 3 = {round(13/3)}")
# # 13 / 3 = 4

# ======================  Логические операторы  ====================
# x = 5
# print(x>5)
# print(x > 3 and x < 5)
# print(x > 3 or x > 8)
# print(not x > 3)

# ======================  Условные операторы  ====================
# num = 5
# if num == 5:
#     print('Five!')
# else:
#     print('Not equal five')

# Если нужно проверить больше 2х вариантов, используется оператор IF для первого варианта,
# ELIF (это означает ELSE IF - "Иначе если") для промежуточных и ELSE  для последнего
# num = 6
# if num == 5:
#     print('Five!')
# elif num < 5:
#     print('Less than five')
# else:
#     print('More than five')

# num = 20
# if 10 < num < 100:
#     print(True)

# message1 = 'hello'
# message2 = 'hellohello'
# if len(message2) > len(message1):
#     print(message2)
# else:
#     print(message1)

# sym1 = 'o'
# sym2 = 'p'
# print(sym1 < sym2)

# ======================  Цикл WHILE  ====================

# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         continue
#         print(i)

# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         break

# Обратный отсчет
# i = 3
# while i > 0:
#     print(i, 'Hello')
#     i = i - 1
# print('Go!')

# ======================  Цикл FOR  ====================

# Для повторения цикла N  раз используем ф-ю range
# for i in range(1, 11, 3):
#     print(i)
#     # 1 - start, 11 - stop, 3 - step

# word = 'hello'
# for symbol in word:
#     print(f'{word.index(symbol)} - {symbol}')

# каждый символ уникальный
# c помощью f можем подставлять динамически
# word = 'hello'
# for index, symbol in enumerate(word):
#     print(f'{index} - {symbol}')
#     # print(f'{index} for {symbol}')

# К FALSE приравниваются следующие  значения:
# print(bool(''))
# print(bool(0))
# print(bool(0.0))
# print(bool([]))
# print(bool({}))
# print(bool(None))

# Все остальные приравниваются к TRUE
# print(bool('0'))
# print(bool(1))
# print(bool('word'))

# arr = ''
# if arr:
#     print('Not empty')
# else:
#     print('Empty')

# ======================  Функция DEF  ====================
def sum_it (x, y):
    result = x + y
    return result

# print(sum_it(5, 8))
# print(sum_it(25, 12))
result = sum_it(65, 89)
print(result)
