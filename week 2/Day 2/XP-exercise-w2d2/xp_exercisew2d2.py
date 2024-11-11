# exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class  Siamese(Cat): 
    pass


all_cats = [Bengal("Mimi", 3), Chartreux("Ivy", 5), Siamese("Daisy", 2)]

saras_pets = Pets(all_cats)
saras_pets.walk()

# Exercise 2 : Dogs
class Dog:
  
    all_dogs_info = {}
    dogs=[]

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.add_to_dogs_info() #it was not in exercise you have to switch it off to run second file
        self.add_name() #it was not in exercise 
        self.what_the_dogs_do() #it was not in exercise 
    def add_to_dogs_info(self):
        Dog.all_dogs_info[self.name] = {
            "age": self.age,
            "weight": self.weight
        }
    def add_name(self):
        Dog.dogs.append(self.name)

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        speed = round((self.weight / self.age) * 10,0)
        print(f"{self.name} runs at {speed} km/hour")
        return speed 
    
    def what_the_dogs_do(self):
        self.bark()
        self.run_speed()

    def fight(self,other_dog):
       self_x = self.run_speed() * self.weight
       other_x = other_dog.run_speed() * other_dog.weight
       if self_x > other_x:
            return f"{self.name} wins the fight!"
       elif self_x < other_x:
            return f"{other_dog.name} wins the fight!"
       else:
            return f"{self.name} and {other_dog.name} are equally strong" 

dog1 = Dog("Nes", 5, 30)
dog2 = Dog("Bobby", 3, 25)
dog3 = Dog("Rusty", 8, 40) 
dogs_fight = [dog1,dog2,dog3]
print(f"You created the instances for the folloing dogs: \n      {Dog.dogs}")
#print(Dog.all_dogs_info) that was not an exercise
for i in range(len(dogs_fight)):
    for j in range(i + 1, len(dogs_fight)):
        print(f"In a fight between {dogs_fight[i].name} vs {dogs_fight[j].name}: {dogs_fight[i].fight(other_dog=dogs_fight[j])}")

#exercise 4 Family
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] > 18
        return False 

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

family = Family("Greenberg")

family.members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
family.born(name='Gigi', age=0.2, gender='Female', is_child=True)
family.family_presentation()

#Exercise 5
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def get_family_details(self):
        return self.members

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Power: {member['power']}, Incredible Name: {member['incredible_name']}")

    def born(self, name):
        new_baby = {
            'name': name,
            'age': 0,
            'gender': 'Unknown',
            'is_child': True,
            'power': 'Unknown Power',
            'incredible_name': f'Baby{name}'
        }
        self.members.append(new_baby)

class TheIncredibles(Family):
    def __init__(self, members, last_name="SuperHeroesISR"):
        super().__init__(members, last_name)
        
    def use_power(self, member_name):
        member_found = False
        for member in self.members:
            if member['name'] == member_name:
                member_found = True
                if member['age'] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old, cannot use power.")
        if not member_found:
            print(f"Member named {member_name} not found in the family.")
    
    def incredible_presentation(self):
        print("Here is our powerful family:")
        print(f"Last Name: {self.last_name}")
        super().family_presentation()
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'},
    {'name': 'Jack', 'age': 16, 'gender': 'Male', 'is_child': True, 'power': 'super speed', 'incredible_name': 'Speedster'}
]


incredible_family = TheIncredibles(members)
incredible_family.incredible_presentation()
incredible_family.born('Jack')
print("\nAfter adding Baby Jack:")
incredible_family.incredible_presentation()
