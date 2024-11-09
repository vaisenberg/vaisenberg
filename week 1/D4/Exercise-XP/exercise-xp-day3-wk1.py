#exercise 1
def display_message():
    print("I am learning Python in this course.")
display_message()

# exercise 2  What’s your favorite book ?

def favorite_book():
    title_book = input("Enter title of your favorite book")
    print(f'One of my favorite books is {title_book}')
favorite_book()

# Exercise 3 : Some Geography

def describe_city(city, country):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")

def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}")
describe_city("Reykjavik")

# exercise 4 Random
import random
def comparison():
    a = int(input('please enter any number from 1 to 100'))
    b = random.randint(1, 100)
    if a == b:
        print("Succes") 
    else:
        print(f'fail The correct number was {b}')
comparison()
# exerecise 5
# Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size="<size>",text="<text>"):


 print(f"The size of the shirt is {size} and the text on the shirt is '{text}'.")

make_shirt()

def make_shirt(size="large",text="I love Python"):


 print(f"The size of the shirt is {size} and the text on the shirt is '{text}'.")

make_shirt()

def make_shirt(size,text="I love Python"):


 print(f"The size of the shirt is {size} and the text on the shirt is '{text}'.")

make_shirt('l')
make_shirt('m')
make_shirt("l","I love my daugter")

#exercise 6 Exercise 6 : Magicians …

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
   for magician in magician_names:
        print(magician)
show_magicians()

def make_great():
   global magician_names
   for magician in magician_names:
    magician = "The Great " + magician 
    print(magician)
make_great()

# exercise 7:
# exercise 7:
import random

def get_random_temp():
    return random.randint(-10, 40)
print("Random temperature:", get_random_temp())

get_random_temp()

def main():
    t = get_random_temp()
    print(f"The temperature right now is {t} degrees Celsius.")
main()

def main_1():
    t = get_random_temp()
    print(f"The temperature right now is {t} degrees Celsius.")
    if t < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= t < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= t <= 23:
        print("between 16 and 23")
    elif 24 <= t < 32:
        print("between 24 and 32")
    elif 32 <= t < 40:
        print("between 32 and 40")

main_1()

def get_random_temp_season(season): 
    
    if season == 'winter':
        return round(random.uniform(-10, 16), 1)  
    elif season == 'spring':
        return round(random.uniform(0, 20), 1)  
    elif season == 'summer':
        return round(random.uniform(16, 40), 1)  
    elif season == 'autumn':
        return round(random.uniform(5, 20), 1)   
    else:
        print("Invalid season entered.")
        return None

def get_season_from_month(month):
    """
    Determines the season based on the month number.
    
    :param month: The month number (1-12)
    :return: The corresponding season as a string.
    """
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'autumn'
    else:
        print("Invalid month number entered.")
        return None

def main_month():
   
    month = int(input("Please enter the month number (1-12): "))
    
 
    season = get_season_from_month(month)
    
    if season:
        
        t = get_random_temp_season(season)
        
        if t is not None:
          
            print(f"The temperature right now is {t} degrees Celsius in {season}.")
            
            
            if t < 0:
                print("Brrr, that’s freezing! Wear some extra layers today.")
            elif 0 <= t < 16:
                print("Quite chilly! Don’t forget your coat.")
            elif 16 <= t <= 23:
                print("between 16 and 23")
            elif 24 <= t < 32:
                print("between 24 and 32")
            elif 32 <= t < 40:
                print("between 32 and 40")
    else:
        print("Please enter a valid month between 1 and 12.")

# Run the main function
main_month()

# exercise 8

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = [] 
    
    for entry in data:
        question = entry["question"]
        correct_answer = entry["answer"]
        user_answer = input(question + "\nYour answer: ").strip()
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}.\n")
            incorrect_answers += 1
            wrong_answers.append((question, correct_answer, user_answer))  

    print(f"Total Correct Answers: {correct_answers}")
    print(f"Total Incorrect Answers: {incorrect_answers}")
    
    if incorrect_answers > 0:
        print("\nIncorrect Answers Summary:")
        for wrong_answer in wrong_answers:
            print(f"Question: {wrong_answer[0]}")
            print(f"Correct Answer: {wrong_answer[1]}")
            print(f"Your Answer: {wrong_answer[2]}\n")

   
        if incorrect_answers > 3:
            print("You have more than 3 wrong answers. You have to play again")
quiz()
