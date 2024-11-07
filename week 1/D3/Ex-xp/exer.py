#exercise 1
numbers_keys = ['Ten', 'Twenty', 'Thirty']
numbers_values = [10, 20, 30]

dict_numbers = dict(zip(numbers_keys, numbers_values))
print(dict_numbers)

#exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
ages_family = list(family.values())
names_family = list(family.keys())
num_tickets = int(len(ages_family))
individual_cost = []
total_cost = 0
i = 0
for i in range(num_tickets):
    if ages_family[i] < 3: 
        individual_cost.append(0)
        total_cost += 0    
    elif 3 <= ages_family[i] <= 12:
        individual_cost.append(10)
        total_cost += 10
    else: 
        individual_cost.append(15)
        total_cost += 15 
    
    print(f"For {names_family[i]} the price for the ticket is $ {individual_cost[i]}")

print(f"Total cost for the tickets is $ {total_cost}")


#Bonus
number_of_tickets = input("How many tickets you will need?")
a = int(number_of_tickets)
library_new = {}

for i in range(a):
    name = input("please eneter your name:")
    age = int(input('please enter your age:'))
    library_new[name]= age

print(library_new)

Exercise 3

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {'France': 'blue', 
                    'Spain': 'red', 
                    'US': ['pink', 'green']
                    }
}
print(brand)
brand["number_stores"] = 2
new_list_clothes = list(brand["type_of_clothes"])
list_conversion = ", ".join(new_list_clothes)
print(f"Zara's customers are: {list_conversion}-owners")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#print(brand)

del brand["creation_date"]
#print(brand)
print(brand["international_competitors"][-1])

new_list_colours_US = list(brand["major_color"]["US"])
UScolours_converse = ", ".join(new_list_colours_US)
print(f"The major clothes colors in the US are: {UScolours_converse}")