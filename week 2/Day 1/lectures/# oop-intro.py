# # oop-intro
# class Dog(): # also if there is no parent - class Dog:
#  pass

# # how to create an instance  - object of the new class

# shelter_dog = Dog() #capital letter ath beginng
# print(type(shelter_dog)) 
# #creating attributes:
# #2 ways of doing
# shelter_dog.name = "Rex"
# print(shelter_dog.name)

# #way 2 _init_
# class Dog:
#     def __init__(self):
       
#         print('the object was created')

# puddle = Dog()

# #creating actual attributes 
# #way 2 _init_
# class Dog:
#     def __init__(self,name,color,age):
#        self.name = name
#        self.colr = color
#        self.age = age
# shelter_dog= Dog('Rexx',"black",7)
# puddle = Dog("Flufy", "white",3)
# print(shelter_dog)
# print(puddle)

# #Exercise
# class Person:
#    def __init__(self,name,age,height):
#     self.name = name
#     self.age = age
#     self.height = height

#     def presentation(self):
#         print(f"Hello, my name is {myself.name}, my age is {myself.age}")
# myself.presentation()
# myself = Person("Olga", 49, 1.72)
# print(myself.name,myself.age,myself.height)



# print(myself.__dict__)
# #how to change attribute 
# myself.age +=1
# print(myself.age)

# Actions - functions inside the class

# class Dog:

#     def __init__(self,name,color,age):
#        self.name = name
#        self.colr = color
#        self.age = age
#     def bark(self):
#        print(f'{self.agename} is barkin')
# shelter_dog= Dog('Rexx',"black",7)
# puddle = Dog("Flufy", "white",3)
# puddle.bark()

# create a method called presentation :

# "Hello, My name is {}, I am {} years old"


# class Dog:

#     def __init__(self,name,color,age):
#        self.name = name
#        self.colr = color
#        self.age = age
#     def bark(self):
#        print(f'{self.agename} is barkin')
#     def walk(self,num_meters):
#        return f"{self.name} walked {num_meters} meters today"
#     # def rename(self,new_name)
#     def rename(self,num_meters):
#        self.name = new_name
    
       
# shelter_dog = Dog('Rexx',"black",7)
# puddle = Dog("Flufy", "white",3)
# puddle.bark()

# puddle.age = 5

# #2 different ways of calling class method 
# Dog.bark(puddle)
# puddle.bark()

