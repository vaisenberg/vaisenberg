#loops  - FOR and WHILE
#for - list
#syntax

students = ['Alex', 'Noah', 'Sara', 'Dima']
            
for each_student in students:
    if each_student == 'Dims':
        print(f'Dobroe Utro,{each_student}')
else:
        print(f'Good morning, {each_student}')


print(f'Welcome, {each_student}')

for i in range(5,10):
    print(f'Hello there {i}')

for i in range(len(students)):
     print(f'Hello There{i}')

for i, each_student in enumerate(students):
     print(1, each_student)

my_nums = [3,5,7,8,10]
print(sum(my_nums))

output = 0
for i in range(len(my_nums)):
     output +=my_nums[i]
print(output)


#WHILE LOOP
i=0
while i < 10:
     print(f'Hi {i}')
     i+=1

family =[]
member = input ('write the family name. press "q" to finish')
while  member != "q":
     member = input ('write the family name. press "q" to finish')
     family.append(member)

print(family)

family = []
keep_asking = True
while keep_asking:
      member = input ('write the family name. press "q" to finish')
      if member == 'Q':
        keep_asking = False
      else:
        family.append(member)
print(family)