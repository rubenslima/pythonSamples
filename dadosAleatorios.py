# pip install Faker
from faker import Faker
fake = Faker('pt_BR')
for _ in range(10):
    # print(fake.name())
    print(fake.name_female())
    print(fake.name_male())
    # print(fake.address())
    # print(fake.job())
    # print(fake.job())