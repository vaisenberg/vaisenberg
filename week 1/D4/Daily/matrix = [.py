# Define the matrix as a 2D list of characters
matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

# Initialize an empty string to collect the decoded message
decoded_message = ""

# Loop over each column and collect only alphabetic characters
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
            decoded_message += char
        else:
            # If there's a non-alpha character, insert a space only if the last character was alphabetic
            if decoded_message and decoded_message[-1].isalpha():
                decoded_message += " "

# Final clean-up of spaces between words
cleaned_message = ' '.join(decoded_message.split())

print(cleaned_message)
