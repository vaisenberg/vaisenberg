#Exercise 1
input_string = input("Enter comma-separated words: ")
sorted_words = ','.join(sorted(input_string.split(',')))

print("Sorted Words:", sorted_words)

# exercise 2
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

sentence = input("Enter the sentence:")
print(longest_word(sentence))