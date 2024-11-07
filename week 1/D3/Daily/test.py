entry_word = (input("please enter a word"))
letter_indexes = {}
for i, letter in enumerate(entry_word):
    if letter in letter_indexes:
        letter_indexes[letter].append(i)
    else: letter_indexes[letter] = [i]
print(letter_indexes)
   

   

