import random

def access_word_list():
    file_path = r'C:\Users\vaise\OneDrive\Desktop\DI-Bootcamp\week 2\Day 4\Exercise-XP\Random Sentence Generator\word_list.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
        if not words:
            print("Error: The file is empty.")
            return []
        
        return words

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def pick_random_words(words, r):
    if len(words) < r:
        print(f"Error: The list contains fewer than {r} words. Adjusting the count.")
        r = len(words)
    random_words = random.sample(words, r) 
    return random_words

def random_sentence(random_words):
    sentence = ' '.join(random_words).lower() 
    return sentence

def main():
    print("This Is Random Sentence Generator! Welcome")
    print("This program generates a random sentence from a list of words.")
    
    try:
        sentence_length = int(input("How many words should the sentence have? (Between 2 and 20): "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    if 2 <= sentence_length <= 20:
        words = access_word_list()
        
        if words:  
            random_words = pick_random_words(words, sentence_length)
            sentence = random_sentence(random_words)
            print(f"Your random sentence is: {sentence}")
        else:
            print("Error: Could not generate sentence due to empty or missing word list.")
    else:
        print("Error: The sentence length must be between 2 and 20 words.")


if __name__ == '__main__':
    main()
