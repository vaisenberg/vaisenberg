class AnagramFinder:
    def __init__(self, word_file):
        try:
            self.word_list = self.load_word_list_from_file(word_file)
            # print("Loaded word list:")
            # print(self.word_list)
        except FileNotFoundError:
            print(f"Error: The file '{word_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def load_word_list_from_file(self, word_file):
        word_list = []
        with open(word_file, 'r') as file: 
            for line in file:
                stripped_line = line.strip()  
                if stripped_line:  
                    word_list.append(stripped_line.lower())  
        return word_list

    def find_anagrams(self, target_word):
        if not target_word:
            print("Error: The target word is empty.")
            return []

        target_word_lower = target_word.lower()
        sorted_target = ''.join(sorted(target_word_lower))  

        anagrams = []

        for word in self.word_list:
            if ''.join(sorted(word)) == sorted_target and word != target_word_lower:
                anagrams.append(word)

        return anagrams
















# class Anagramfinder:
#     def __init__(self, word_file):
        
#         self.word_list = self.load_word_list_from_file(word_file)
#         print("Loaded word list:")
#         print(self.word_list)



#     def load_word_list_from_file(self,word_file):
#          with open(word_file, 'r') as file:
#             return [line.strip() for line in file]
        
           