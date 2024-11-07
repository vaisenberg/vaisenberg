#Data Structure:
#sequences = string
#data structure sequence: list
#sets
#tuplets
my_name = "Julina"
last_name = "Schmidt"
nickname = "ju05"
#two options to create a list
user_info = [my_name,last_name,nickname] #wrap with squre brackets
user_name = list(my_name) #built - in method list()

option1 = ["Jullian"]
option2 = list("Juliana")

print(user_info)
print(user_name)

print(option1)
print(option2)

#methods for list:
num_list = [1,2,4,7,8,12]
num_list.append(120) # at the end
print(num_list)
num_list.insert(2,55) # 3rd in list will 55
print(num_list)

num_list.remove(2) #removes(only elements) first number 2
print(num_list)
del num_list[3]
print(num_list)

num_list.pop() #delets the last element
print(num_list)

num_list.pop(3) #deletes 4rd index
deleted_el = num_list.pop(3) # stores the deleted index
print(deleted_el)

print(num_list.index(4)) # takes the element to index
num_list[2] = 40 #reasigning the value
print(num_list)

print(num_list[4:])
print(num_list[3:5])

#tuples: unmutable sequence

some_tuple = tuple()
my_tuple = (10,45,33,67)
#unpack a tuple
score1, score2, score3, score4 = my_tuple
print(score1)
print(score2)
print(score3)

print(my_tuple[-1])

my_tuple_list = list(my_tuple) # converting tuple to a list
print(my_tuple_list)

# list1 = [5,10,15,20,25,50,20]
# if list1(20):
#     list1[list1.index(20)] = 200
# else: print("number not found")
# print(list1)

#SETS : UNORDERED And does not accept multiple occurence
my_set = {"Juliana"}
my_set = set()

my_set.add('Rick')
my_set.add("Morty")
my_set.add("Rick")

set2={"harry","Ron","Morty"}
set3 = my_set.intersection(set2)
print(set3)

set4 = my_set.union(set2)
print(set4)

#deleting information in a list - convert it to a set and then back to a list

names = ['Leah', 'Luke', 'Chubaca', 'Harry', 'Harry']
names_set = set(names)
print(names_set)

names = list(names)
print(names)

fruits = ['lime', 'apple', 'banana']

friuts2 = fruits.copy()
print(fruits)
print(friuts2)











