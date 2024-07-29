# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# print(factorial(5))


# RECURSION - это когда ф-я вызывает саму себя
# c помощью рекурсии

# проверяет переменную > 0 ил нет, если она = 0 или отриц. число то выдает 1
# а если > 0 то тогда идет расчет
# (factorial 6)
# (* 5 (factorisl 5))
# (* 6 ( * 5  (factorisl 4)))
# (* 6 ( * 5 ( * 4  (factorial 3))))
# (* 6 ( * 5 ( * 4 ( * 3  (factorisl 2)))))
# (* 6 ( * 5 ( * 4 ( * 3 ( * 2 (factorisl 1))))))
# (* 6 ( * 5 ( * 4 ( * 3 ( * 2  1)))))
# (* 6 ( * 5 ( * 4 ( * 3 2))))
# (* 6 ( * 5 ( * 4 6))
# (* 6 ( * 5  24))
# (* 6 120))
# 720

# def factorial1(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial1(n - 1)
#
# print(factorial1(5))

