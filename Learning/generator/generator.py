from fuction_generator.data import User
from faker import Faker

faker_en = Faker("En")
Faker.seed()

def generator_user():
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        phone_number=faker_en.phone_number()
    )

a = next(generator_user())
print(a.first_name)
print(a.last_name)
print(a.phone_number)