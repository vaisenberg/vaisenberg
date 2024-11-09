entry_word = (input("please enter a word"))
letter_indexes = {}
for i, letter in enumerate(entry_word):
    if letter in letter_indexes:
        letter_indexes[letter].append(i)
    else: letter_indexes[letter] = [i]
print(letter_indexes)
   
# #daily chalenge day 3 week 1
# #1
# for num_list in range(1, 21):  
#     print(num_list)

# for num in range(1, 21):  
#     if (num - 1) % 2 == 0:  
#         print(num)

# #2

# my_name = "Olga"


# while True:
#     user_name = input("Please enter your name: ")  
#     if user_name.title() == my_name:  
#         print(f"Hello, {my_name}!")
#         break 
#     else:
#         print("That's not my name. Try again!") 

