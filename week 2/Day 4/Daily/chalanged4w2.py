import string
import nltk
from nltk.corpus import stopwords


class Text:
    def __init__(self, text):
        # Initialize the text attribute and store the cleaned-up list of words
        self.text = text
        self.words = self._clean_text(text)
    
    def _clean_text(self, text):
        """Cleans the text and returns a list of words."""
        text = text.lower()  
        words = text.split()  
        return words

    def word_frequency(self, word):
        """Returns the frequency of a specific word in the text."""
        word = word.lower()  # To make it case-insensitive
        if not self.words:  # If the words list is empty, return a meaningful message
            return None
        return self.words.count(word)
    
    def most_common_word(self):
        """Returns the most common word in the text."""
        if not self.words:
            return None
        word_count = {}
        for word in self.words:
            word_count[word] = word_count.get(word, 0) + 1
        most_common = max(word_count, key=word_count.get)
        return most_common
    
    def unique_words(self):
        """Returns a list of all unique words in the text."""
        if not self.words:
            return []
        return list(set(self.words))  # Use set to get unique words

class TextModification(Text):
    def __init__(self, text):
        # Initialize the base Text class
        super().__init__(text)
    
    def remove_punctuation(self):
        """Returns the text without any punctuation."""
        # Use the string.punctuation to get all punctuation characters
        table = str.maketrans('', '', string.punctuation)
        text_without_punctuation = self.text.translate(table)
        return text_without_punctuation
    
    def remove_stopwords(self):
        """Returns the text without any English stopwords."""
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in self.words if word not in stop_words]
        return ' '.join(filtered_words)
    
    def remove_special_characters(self):
        """Returns the text without any special characters."""
        # Filter out any characters that are not letters or numbers
        cleaned_text = ''.join([char for char in self.text if char.isalnum() or char.isspace()])
        return cleaned_text

# Example usage:

# Text string
text = ""

# Create an object of TextModification
my_text = TextModification(text)

# Remove punctuation
print("Text without punctuation:", my_text.remove_punctuation())

# Remove stopwords
print("Text without stopwords:", my_text.remove_stopwords())

# Remove special characters
print("Text without special characters:", my_text.remove_special_characters())
