from function_Декораторы_Лямбда import *
import function_Декораторы_Лямбда as f
result = f.hello('Anna')
print(result)
# Закоментировала 72 - иначе срабатывает декоратор

def introduce(**kwargs):
    print(type(kwargs))
    print(kwargs)

(introduce(name='Mario', lname='Smith', position='QA'))

def my_result(*arg):
    print(type(arg))
    print(sum(arg))

my_result(5, 8, 9, 70)
