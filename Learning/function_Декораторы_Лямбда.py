# LESSON 4
# ===========================  ТИПЫ АРГУМЕНТОВ =========================

# =======  POSITIONAL ARGUMENTS (Позиционные) ==========
# Значения копируются в соответствующие параметры по порядку

# ======= KEYWORD ARGUMENTS (Именованные) ============
# Передаются как пара "имя=значения" в любом порядке

# def sum_it(a, b, c = 5):
#     return a + b + c
# print(sum_it(5, 4))
# print(sum_it(5, 4, c = 10))
# будет ошибка в этом случае
# print(sum_it(c = 10, 5, 4))

# def hello(fname, lname, age):
#     return f'Hello, my name is {fname} {lname}. I am {age} yesrs old'
#
# # print(hello(age=25, fname='Anna', lname='Smith'))
#
# def pattern(length, char1='/', char2='*'):
#     return (char1 + char2) * length + char1
#
# print(pattern(9, char1='-'))

# ====  встроенные ф-и

# min_value = min(5, 8, 25, 1, 0)
# print(min_value)

# ============  NAMESPACE (ПРОСТРАНСТВО СЛОВАРЕЙ)  ============

# Это место, где ханится переменная
# === BUILT-IN (встроенное пространство) ===
# === GLOBAL ===
# === ENCLOSED (замкнутое) ===
# === LOCAL  ===

# =====================    ЗАМЫКАНИЕ    =======================
name = 'Alice'
# def outer_function():
#     # name = 'Alex'
#     def inner_function():
#         # name = 'Albert'
#         return name
#     return inner_function
#
# enclosure = outer_function()
# result = enclosure()
# print(result)

# =====================    ДЕКОРАТОРЫ    =======================
# Представляют ф-ю, которая в качестве параметра получает ф-ю и в качестве результата также возвращает ф-ю
# Декоратор позволяет обернуть  другую ф-ю для расширения ее ф-ти без непосредственного изменения ее кода

def decorator_function(func):
    def wrapper(*arg):
        print('Wrapper function!')
        print(f'Wrapped function: {func.__name__}')
        print(f'Execiting wrapper function')
        print(func(*arg))
        print('Exiting wrapper function')
    return wrapper

# вложенная ф-я
@decorator_function
def my_wrapper(item):
    return f'{item} is wrapped!'

my_wrapper('Candy')

# @decorator_function
def hello(name):
    return f'Hello, My name is {name}'

hello('Alex')

x = 5
y = 10
def sum_it2(x, y):
    print(f'locals: {locals()}')
    return x + y

# print(f'Inside the fuction: {sum_it2(5, 8)}')
# print(f'Outside the function: {x + y}')
# print(f'Globals: {globals()}')

# import math
# arr = [1, 5, 8, 9, 10, 25]
# result = math.prod(arr)
# print(result)
# # или с помощью алияс
# import math as m
# arr = [1, 5, 8, 9, 10, 25]
# result = m.prod(arr)
# print(result)

import datetime
birth_year = 1985
curretn_date = datetime.date.today()
curretn_age = curretn_date.year - birth_year
print(curretn_date)
print(curretn_age)

# =====================    LAMBDA (АНОНИМНЫЕ Ф-И: ЛЯМБДА-ВЫПАЖЕНИЯ    =======================
# Анонимные ф-и могут модержать лищь одно выражение, но и выполняются быстрее
# В отличии от обычных ф-й, их не обязательно присваивать переменной
# не требует инструкции return

res = lambda x, y:x * y
print(res(2, 5))

def take_odd(num):
    if num%2:
        return True
    return False

# только нечетные отфильтровать
l = [1, 5, 8, 12, 15]
new_l = list(filter(lambda x: x%2, l))
print(new_l)

# только четные отфильтровать
new_n = list(filter(lambda x: x%2==0, l))
print(new_n)

# замена for loop
my_list = ['Hi', 'ananas', 2, 75, 'pizza', 100]
new_l2= list(filter(lambda item: isinstance(item, str) and 'a' in item, my_list))
print(new_l2)