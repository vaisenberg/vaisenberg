class AnagramFinder:
    def __init__(self, word_file):
        try:
            self.word_list = self.load_word_list_from_file(word_file)
            # Debugging: print the loaded word list
            # print("Loaded word list:")
            # print(self.word_list)
        except FileNotFoundError:
            print(f"Error: The file '{word_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_word_list_from_file(self, word_file):
        # Read the file and return a list of cleaned words (convert to lowercase)
        word_list = []
        with open(word_file, 'r') as file:  # The 'with' statement ensures the file is closed after reading
            for line in file:
                stripped_line = line.strip()  # Remove leading/trailing whitespace
                if stripped_line:  # Check if the line is not empty
                    word_list.append(stripped_line.lower())  # Convert to lowercase and append
        return word_list

    def find_anagrams(self, target_word):
        # Handle empty target_word case
        if not target_word:
            print("Error: The target word is empty.")
            return []

        # Convert target_word to lowercase before sorting
        target_word_lower = target_word.lower()
        sorted_target = ''.join(sorted(target_word_lower))  # Convert target word to lowercase

        # Initialize an empty list to store the anagrams
        anagrams = []

        # Loop through the word list to find anagrams
        for word in self.word_list:
            # Sort the word and check if it's an anagram and not the target word itself
            if ''.join(sorted(word)) == sorted_target and word != target_word_lower:
                anagrams.append(word)

        return anagrams

# Test the code
anagram_finder = AnagramFinder('word_list.txt')

# Test with target word 'water'
anagrams = anagram_finder.find_anagrams('price')
print("Anagrams found:")
print(anagrams)














# class Anagramfinder:
#     def __init__(self, word_file):
        
#         self.word_list = self.load_word_list_from_file(word_file)
#         print("Loaded word list:")
#         print(self.word_list)



#     def load_word_list_from_file(self,word_file):
#          with open(word_file, 'r') as file:
#             return [line.strip() for line in file]
        
           