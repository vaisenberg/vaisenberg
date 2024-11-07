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
float_list = [x * 0.5 + 1 for x in range(3, 11)]
print(float_list)

def float_sequence(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step
for num in float_sequence(1.5, 5.5, 0.5):
    
    print(num)

#exercise 5
for number in range(1, 21):
    print(number)

for number_new in range(1, 21):
    if number_new % 2 == 0:
        print(number_new)
