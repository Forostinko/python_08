from dataclasses import dataclass

"""Создаем генератор в папке generator
сайт    -     https://faker.readthedocs.io/en/master/"""

@dataclass
class User:
    first_name: str = None,
    last_name: str = None
    phone_number: str = None