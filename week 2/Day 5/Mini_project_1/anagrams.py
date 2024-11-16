from anagramcheker import AnagramFinder

anagram_finder = AnagramFinder('word_list.txt')

while True:
    print("\nWelcome to Anagrams Generator")

   
    action = input("\nChoose an action - (Type 'find' to search for anagrams, or press Enter to exit): ").lower()

    
    if action == "find":
       
        word = input('Enter a word for which you want to see its anagrams: ').lower()

       
        if word == "":
            print("Exiting Word Anagram Generator!")
            break  
        if word not in anagram_finder.word_list:
            print(f"YOUR WORD: '{word.upper()}'\nThis is NOT a valid English word.")
        else:
          
            anagrams = anagram_finder.find_anagrams(word)

            if anagrams:
                print(f"YOUR WORD: '{word.upper()}'\nThis is a valid English word.\nAnagrams for your word: {', '.join(anagrams)}.")
            else:
                print(f"YOUR WORD: '{word.upper()}'\nThis is a valid English word.\nNo anagrams found for your word.")
    elif action == "":
        print("Goodbye! Exiting the program.")
        break  

    else:
        print("Invalid action. Please type 'find' to search for anagrams or press Enter to exit.")




