# Лямбда - это анонимная ф-я, короткая запись

# в lst 6 а в lst2 7, значит бужет 6 и 1000 пропадет


#  =====================    FUNCTION MAP   ========================
# map - возвращает лист
# если нам что- то нужно найти то мы сначала сортируем
# а потом находим каое-то значение, н-р min (или с помощью ф-и min)

# lst = [1, 3, 5, 7, 8, 9]
# lst2 = reversed(lst)
# # revesed -> 1+9, 3+8, 5+7
# lst2 = [3, 8, 6, 7, -2, -6, 1000]
#
# print(lst2)
#
# # # sum_2 = list(map(lambda x: x + 2, lst))
# # print(sum_2 := list(map(lambda x: x + 2, lst)))
# # print(sum_2)
# # # распечатает в столбик
# # print(*sum_2, sep='\n')
#
#
# def myfunc(a, b, c):
#     return a + b + c
#
# print(list(map(myfunc,(1, 5, 8), (3, 6, 9), (5, 7, 1))))
#
# def myfunc(a, b):
#     return a + b
#
# print(list(map(myfunc, lst, lst2)))
# # взял лист созданный в самом начале - пробегается по листу - он его складывает
# # map - пробегается по всем интерируемым обьектам которые мы передали - a и b
# # берет из каждых этих обьектов по первому значению передает в эту ф-ю в качестве аргументов
# # и затем формирует лист
#
# # 1 3 5 7 9 11
# # arr = list(map(int, input().split()))
# # arr = list(map(float, input().split()))
# # arr = list(map(str, input().split()))
# # arr = list(map(lambda  x: int(x)*int(x), input().split()))
# # print(arr)
#
# # arr = map(lambda x: int(x)*int(x), temp := input().split())
# # # выдаст object, получаем адрес map
# # print(arr)
# # #выдаст теже самые значения
# # print(*arr)
#
# a, b, c, d ,f, g = map(lambda x: int(x)*int(x), temp := input().split())
# # # a, *b, c = map(lambda x: int(x)*int(x), temp := input().split())
# # print(a)
# # print(b)
# # print(c)
# # print(temp)
#
# # a = map(str, temp := input().split())
# # a = map(lambda x, y: int(x) * int(y), temp := input().split(), [6,8, 1, -10, -5, 10])
# # print(*a)
# # print(temp)


#    ===================   FUNCTION FILTER   =============================

lst = [1, 3, 5, 7, 8, 9]
lst2 = [3, 8, 6, 7, -2, -6, 1000]
lst3 = ['dog', 'cat', 'rabbit', 'owl']
#
# # res = filter(lambda  x: x > 4, lst)
# # print(*res)
# #
# # # поиск мах значения
# # res = lambda x, y: x if x > y else y
# #
# # # тоже самое что ф-я
# # def res2(a, b):
# #     return a if a > b else b
# #
# # print(res(-100000, lst2[-1]))
# # print(res(-100000, lst2[-1]))
#
# # все четные значения и положительные
# #                          что                     где
# print(list(filter(lambda x: x % 2 == 0 and x > 0, lst2)))
# print(list(filter(lambda x: x % 2 == 0 and x > 0 and x < 100, lst2)))
#
# print(list(filter(lambda x: len(x) < 5, lst3)))
#
# # =======  Эти 2 записи идентичны   ==========
#
# # большими буквами
# print([i.upper() for i in list(filter(lambda  x: len(x) < 5, lst3))])
#
# # фильтр отфильтровал значения в lst3 -> затем map использует перебор и
# # пробегается и преобразует в upper
# print(list(map(lambda y: y.upper(), list(filter(lambda  x: len(x)< 5, lst3)))))

def uppers(x):
    return x.upper()

print(list(map(uppers, list(filter(lambda y: y.upper(), )))))
print(list(map(uppers, list(filter(lambda x: len(x) < 5, lst3)))))


#    ===================   FUNCTION REDUSE   =============================

# нужно импортировать из библиотеки functools
# метод reduce пробегается и выдает какой то рез-т ф-ю
# sum - зарезервировано, поэтому чтобы отличать sum_

from functools import reduce

# lst = [1, 3, 5, 7, 8, 9]
# lst2 = [3, 8, 6, 7, -2, -6, 1000]
# lst3 = ['dog', 'cat', 'rabbit', 'owl']

# sum_ = reduce(lambda  x, y: x + y, lst)
# sum_ = reduce(lambda  x, y = 0: x + 10 if x > y else x - 10, lst2)
#
# # max значение
# sum_ = reduce(lambda  x, y: x if x > y else y, lst2)
# # min значение
# sum_ = reduce(lambda  x, y: x if x < y else y, lst2)
# sum_ = reduce(lambda  x, y: x if x < y else y, lst, 100)
#
# sum_ = reduce(lambda  x, y: x if x < y else y, lst2, -10)
# sum_ = reduce(lambda  x, y: x if x < y else y, lst2, -1)
#
# print(sum_)


