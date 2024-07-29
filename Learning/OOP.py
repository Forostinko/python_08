# LESSON 5 - наследование
# Класс - это шаблон кода, по которому создаются обьекты, имеющие общую структуру и обдадающие
# одинаковым поведением. Сам по себе класс ничего не делает, но с его помощью можно создать обьект и использовать
# его в работе
# Обьект - это экземпляр класса
# У каждого обьекта есть свойства(атрибуты) и поведение(методы)

class Person:

    country = 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def hello(self):
        return f'{self.fname} {self.lname} says hello'

#     полиморфизм
    def learn(self):
        return f'I\'m learning'

class Programmer(Person):
    def __init__(self, fname, lname, language, job_title, salary):
        super().__init__(fname, lname)
        self.language = language
        self.job_title = job_title
        self.__salary = salary

    def coding(self):
        return f'I\'m coding with {self.language}'
# \ говорим - воспринимай как знак препинания

# чтобы взаимодействовать с salsry 10000 пишем метод
    def get_salary(self):
        return self.__salary

#     полиморфизм
    def learn(self):
        return f'I\'m learning coding'

    # Инкапсуляция
    # переписываем первоначальное значение и становится новым значение нашего
    # приватного св-ва
    def set_salary(self, new_salary):
        self.__salary = new_salary


class Tester(Person):
    def __init__(self, fname, lname, framework, job_title):
        super().__init__(fname, lname)
        self.framework = framework
        self.job_title = job_title

    def testing(self):
        return f'I\'m testing with {self.framework}'

#     полиморфизм
    def learn(self):
        return f'I\'m learning trsting'


person_1 = Person('Alex', 'Baker')
# print(person_1.fname)
# print(person_1.lname)

# Можем переписать наши св-ва
person_1.fname = 'Alexander'
# print(person_1.__dict__)
# print(person_1.hello())
print(person_1.country)

# стр 43  и пото добавть на 57 salary - 10000
print(person_1.fname)
print(person_1.__dict__)
# полиморфизм
print(person_1.learn())



person_2 = Person('Kevin', 'Smith')
print(person_2)

coder_1 = Programmer('Alexandro', 'Vill', 'Python', 'Senior developer', 10000)
# print(coder_1.lname)
# print(coder_1.language)
# print(coder_1.job_title)
# print(coder_1.coding())
# print(coder_1.country)
print(coder_1.get_salary())
print(coder_1.set_salary(20000))
# полиморфизм
print(coder_1.learn())
# доступ к приватному обьекту напрямую, если при . - не появляется список(не рекомендуется так!)
print(coder_1._Programmer__salary)
print(coder_1._Job_title)


#
tester_1 = Tester('Olga', 'Popova', 'pytest', 'SDET')
# print(tester_1.fname)
# print(tester_1.framework)
# print(tester_1.testing())
# print(tester_1.country)
print(tester_1.learn())

