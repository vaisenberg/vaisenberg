#Daily chalange w1_day1
#Chalage 1
entry_word = (input("please enter a word"))
letter_indexes = {}
for i, letter in enumerate(entry_word):
    if letter in letter_indexes:
        letter_indexes[letter].append(i)
    else: letter_indexes[letter] = [i]
print(letter_indexes)

#challenge 2.1
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"
value_wallet = int(wallet.replace('$', ''))  
spending = 0
swapped_dict = {}
swapped_dict_back = {}


for key, value in items_purchase.items():
    cleaned_value = value.replace('$', '').replace(',', '')
    int_value = int(cleaned_value)
    if int_value not in swapped_dict:
        swapped_dict[int_value] = [key]
    else:
        swapped_dict[int_value].append(key)

sorted_dict = dict(sorted(swapped_dict.items()))

for price, items in sorted_dict.items():
    for item in items:
        if item not in swapped_dict_back:
            swapped_dict_back[item] = price

#print("Swapped dictionary reversed (items back to prices):", swapped_dict_back)

items_to_remove = []
for item, price in swapped_dict_back.items():
    if spending + price <= value_wallet:
        spending += price  
    else:
        items_to_remove.append(item)
        wallet_check = spending
for item in items_to_remove:
    del swapped_dict_back[item]

#print("Items remaining in basket after exceeding wallet limit:", swapped_dict_back)

basket_list =sorted(swapped_dict_back.keys())
if wallet_check == 0:
    print('nothing')
else:
    print(basket_list)

    #challenge 2.2
items_purchase = {
    "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100"
value_wallet = int(wallet.replace('$', ''))  
spending = 0
swapped_dict = {}
swapped_dict_back = {}


for key, value in items_purchase.items():
    cleaned_value = value.replace('$', '').replace(',', '')
    int_value = int(cleaned_value)
    if int_value not in swapped_dict:
        swapped_dict[int_value] = [key]
    else:
        swapped_dict[int_value].append(key)

sorted_dict = dict(sorted(swapped_dict.items()))

for price, items in sorted_dict.items():
    for item in items:
        if item not in swapped_dict_back:
            swapped_dict_back[item] = price

#print("Swapped dictionary reversed (items back to prices):", swapped_dict_back)

items_to_remove = []
for item, price in swapped_dict_back.items():
    if spending + price <= value_wallet:
        spending += price  
    else:
        items_to_remove.append(item)
        wallet_check = spending
for item in items_to_remove:
    del swapped_dict_back[item]

#print("Items remaining in basket after exceeding wallet limit:", swapped_dict_back)

basket_list =sorted(swapped_dict_back.keys())
if wallet_check == 0:
    print('nothing')
else:
    print(basket_list)

     #challenge 2.3
items_purchase = {
    "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$100"
value_wallet = int(wallet.replace('$', ''))  
spending = 0
swapped_dict = {}
swapped_dict_back = {}


for key, value in items_purchase.items():
    cleaned_value = value.replace('$', '').replace(',', '')
    int_value = int(cleaned_value)
    if int_value not in swapped_dict:
        swapped_dict[int_value] = [key]
    else:
        swapped_dict[int_value].append(key)

sorted_dict = dict(sorted(swapped_dict.items()))

for price, items in sorted_dict.items():
    for item in items:
        if item not in swapped_dict_back:
            swapped_dict_back[item] = price

#print("Swapped dictionary reversed (items back to prices):", swapped_dict_back)

items_to_remove = []
for item, price in swapped_dict_back.items():
    if spending + price <= value_wallet:
        spending += price  
    else:
        items_to_remove.append(item)
        wallet_check = spending
for item in items_to_remove:
    del swapped_dict_back[item]

#print("Items remaining in basket after exceeding wallet limit:", swapped_dict_back)

basket_list =sorted(swapped_dict_back.keys())
if wallet_check == 0:
    print('nothing')
else:
    print(basket_list)