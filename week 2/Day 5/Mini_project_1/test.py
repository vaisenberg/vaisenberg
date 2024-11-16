class AnagramFinder:
    def __init__(self, word_file):
        try:
            self.word_list = self.load_word_list_from_file(word_file)
            # Debugging: print the loaded word list
            print("Loaded word list:")
            print(self.word_list)
        except FileNotFoundError:
            print(f"Error: The file '{word_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_word_list_from_file(self, word_file):
        # Read the file and return a list of cleaned words (convert to lowercase)
        with open(word_file, 'r') as file:
            return [line.strip().lower() for line in file if line.strip()]  # Convert to lowercase

    def find_anagrams(self, target_word):
        # Handle empty target_word case
        if not target_word:
            print("Error: The target word is empty.")
            return []

        # Convert target_word to lowercase before sorting
        target_word_lower = target_word.lower()
        sorted_target = ''.join(sorted(target_word_lower))  # Convert target word to lowercase
        print(f"Sorted target word: {sorted_target}")  # Debugging: print sorted target word

        # Initialize an empty list to store the anagrams
        anagrams = []

        # Loop through the word list to find anagrams
        for word in self.word_list:
            # Sort the word and check if it's an anagram and not the target word itself
            if ''.join(sorted(word)) == sorted_target and word != target_word_lower:
                anagrams.append(word)

        # Debugging: show the result
        print(f"Anagrams found for '{target_word}': {anagrams}")
        return anagrams

# Test the code
anagram_finder = AnagramFinder('word_list.txt')

# Test with target word 'MEAT'
anagrams = anagram_finder.find_anagrams('water')
print("Anagrams found:")
print(anagrams)



