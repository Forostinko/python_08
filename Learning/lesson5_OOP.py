# [count, __init__, greet, get_fullname, add_one, ban, __str__]
class User:
    # Атрибут класса
    count = 0
    # ======================     Методы    ======================

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._ban = False
        self.add_one()

    def greet(self):
        print(f'Привет, {self.get_fullname()}!')


    # =====   Метод экземпляра - у него есть self, есть доступ к хкземляру класса
    # у которого он вызывается (self)
    def get_fullname(self):
        return f'{self.name} {self.surname}'


    # =====    Статический метод вообще не имеет доступ (). Но может принимать аргументы
    # @staticmethod
    # def function(self):
    #     print('Статический метод')

    # Но может принимать аргументы
    @staticmethod
    def function(age):
        return age > 18

    # =====    Метод класса имеет доступ к классу (cls)
    @classmethod
    def add_one(cls):
        cls.count += 1

    def __str__(self):
        return self.get_fullname()

    @property
    def ban(self):
        return self._ban


# Унаследовали и переписали от своего род.класса все методы и атрибуты т.к. указали (User)
# [count, __init__ (ДОПОЛНИЛИ), greet (ПЕРЕПИСАЛИ), get_fullname, add_one, ban, __str__]
class PremiumUser(User):

    def __init__(self, name, surname, description):
        # через метод super обратились к родительскому __init__ и передали параматры
        # создали свой атрибут desk
        super().__init__(name,surname)
        self.description = description

    def greet(self):
        print(f'***Привет, {self.get_fullname()}!***')

pr_user = PremiumUser('Mike', 'Smith', 'Всем привет!')
pr_user.greet()
print(pr_user.desk)


user_1 = User('John','Smith')
user_2 = User('Slava', 'Morozov')

# вызываем age
# print(user_2.function(29))

# user_1.greet()
# print(user_2.get_fullname())
# print(user_1)  # __str__
# print(1)  # __str__, __add__



# "def _", "_num = 1000"    переменная или ф-я с защитой,которую не нужно трогать -
# можем добраться через гетер и сетер
# если "__ban"  - это двойная защита и сложно до него добраться (только через костыль)
#     def _cmp(x, y):
#         return 0 if x == y else 1 if x > y else -1
#     # константа - большими буквами
#     MINYEAR = 1
#     MAXYEAR = 9999
#     _MAXORDINAL = 3652069

