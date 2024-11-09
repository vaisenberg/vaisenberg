#exercise 1
my_fav_numbers = {7, 13, 21, 19, 2006}
print(my_fav_numbers)

my_fav_numbers.add(4)
my_fav_numbers.add(11)
print(my_fav_numbers)

friend_fav_numbers = {7, 10, 13}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#exercise 2
# No- you can not add to a tuple, but you can convert it to a list ,
#then add integer, and convert it to a new tuple

#exercise 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#print(basket)
basket.remove('Banana')
basket.append("Kiwi")
basket.insert(0,'Apples')
#print(basket)
basket.count("Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

#exercise 4
#float is a number with the decimal
#integer is a number without decimal point

sequence_numbers = []
print_num = []
i = 1.5
while i <= 5:
    sequence_numbers.append(i)
    i += 0.5 
for i in sequence_numbers:
    if i == int(i):
        print_num.append(int(i))  
    else:
        print_num.append(i)  
print(print_num)

#exercise 5
for number in range(1, 21):
    print(number)

for number_new in range(1, 21):
    if number_new % 2 == 0:
        print(number_new)

# Exercise 6 


my_name = "Olga"
while True:
    user_name = input("Please enter your name: ")  
    if user_name.title() == my_name:  
        print(f"Hello, {my_name}!")
        break 
    else:
        print("That's not my name. Try again!") 

#exercice 7


favorite_fruits = input("Please input your favourite fruits, ensure that you use space between each fruit: ").split()


print(favorite_fruits)

word_fruit = input("Please, please enter any fruit you want to eat")

for i in favorite_fruits:
    if i == word_fruit:
        print('You chose one of your favorite fruits! Enjoy!')
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8: 
list_toppings = []
base_pizza = 10
pizza_price = 0
while True: 
    
    topping=input('please enter your topping, if yoy do not want to add topping, ender: quit').strip()
    if topping.lower() == "quit":
        break
    list_toppings.append(topping)
    print(f'Your added a topping {topping}')
pizza_price = base_pizza + 2.5 * len(list_toppings)
print("\nYour pizza has the following toppings:")
for topping in list_toppings:
    print(f"- {topping}")

print(f"\nTotal price: ${pizza_price:}")
print(pizza_price)

# Exercise 9: Cinemax


num_family_members = int(input("please enter a number of people watching a movie?"))
age_list = []
total_price = 0
for i in range(num_family_members):
    age = int(input(f'Please enter the age for person {i+1}: '))
    age_list.append(age)
    if i in range(num_family_members):

        for age in age_list:
            if age <= 3:
                price = 0 
            elif 3 < age <= 12:
                price = 10 
            else:
                price = 15  
                
    total_price =+ price 
print(f"Total cost of your family tickets: ${total_price}") 

# exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", 
                   "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")