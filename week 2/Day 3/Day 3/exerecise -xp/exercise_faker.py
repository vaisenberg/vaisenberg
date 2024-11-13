# exercise 6f

from faker import Faker

fake = Faker()


users = []

def add_user():

    user_data = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
  
    users.append(user_data)


for i in range(5):  
    add_user()

print(users)