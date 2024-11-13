# DATA STRUCTURES:
# sequences = string
# data structure sequence: list
# sets
# tuples

# my_name = 'Juliana'
# last_name = "Schmidt"
# nickname = 'ju05'

# # # two options to create a list
# user_info = [my_name,last_name,nickname] # wrap with square brackets []
# user_name = list(my_name)# use built-in method list()

# option1 = ['Juliana']
# option2 = list('Juliana')

# print('option 1', option1)
# print('option 2', option2)

# print(user_info)
# print(user_name)


# nums_list = [1,2,4,7,2,8,12]

#list indexing
# print(nums_list[4:])
# print(nums_list[3])

#methods for list
# nums_list.append(120)
# print(nums_list)

# nums_list.insert(2,55)  #insert(index,element)
# print(nums_list)

# nums_list.remove(2)#remove(element)
# print(nums_list)

# del nums_list[3] #how to delete an index
# print(nums_list)

# # nums_list.pop() #default: deletes the last element
# deleted_el = nums_list.pop(3) #pop(index): delete the element in this index and save what was deleted
# print(deleted_el)

# print(nums_list.index(4)) #index(element)
# nums_list[2] = 40
# print(nums_list)


# # ex1
# list1 = [5, 10, 15, 20, 25, 50, 20]

# if list1.index(20):
#    list1[list1.index(20)] = 200
# else: print('number not founded')

# print(list1)

#tuples: unmutable sequence

# some_tupple = tuple()
# scores = (10,45,33,67)

# #unpack a tuple
# score1, score2, score3, score4 = scores

# print(score1)
# print(score2)
# print(score3)

# #indexing tuples
# print(scores[-1])

#how to work around to change a tuple:

#convert the tuple to a list
# scores_list = list(scores)
# scores_list.append(120)

# #convert the list back to a tuple
# updated_tuple = tuple(scores_list)
# print(updated_tuple)

# print(type(updated_tuple))

#SETS: Unordered and doesn't accept multiple occurences

# my_set = {''}
# my_set = set()

# my_set.add('Rick')
# my_set.add('Morty')
# my_set.add('Rick')

# #{'Rick', 'Morty'}

# set2 = {'Harry','Ron','morty'}

# set3 = my_set.intersection(set2)
# print(set3)

# set4 = my_set.union(set2)
# print(set4)

# names = ['Leah', 'Luke', 'Chubaca', 'Harry', 'Harry']

# names_set = set(names)
# print(names_set)

# names = list(names_set)
# print(names)

# fruits = ['lime', 'apple', 'banana']

# # fruits2 = fruits.copy()
# fruits2 = fruits


# print(fruits)
# print(fruits2)
# fruits2.append('kiwi')
# print(fruits)
# print(fruits2)








