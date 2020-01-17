
# Takes a given input from the user and converts it to leetspeak.

phrase = str(input("What is the phrase you would like to translate? ")).upper()

# Lists of characters and characters to replace them.

chars = ["A", "E", "G", "I", "O", "S", "T"]

new_chars = ["4", "3", "6", "1", "0", "5", "7"]

# Loop that iterates through the list and finds the index and replaces them in the phrase.

for letter in chars:
    index = chars.index(letter)
    phrase = phrase.replace(chars[index], new_chars[index])
print(phrase)
    