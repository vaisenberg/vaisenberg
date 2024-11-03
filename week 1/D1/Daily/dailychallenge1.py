str_1 = input("please enter a string containing 10 charachters")
str_2 = str_1.strip("")
if len(str_2)< 10:
    print(" string is not long enough")
elif len(str_2) > 10:
    print("string too long")
if len(str_2) ==10:
    print("perfect string")
print(((str_1)[0]) + (f'\n{(str_1)[-1:]}'))