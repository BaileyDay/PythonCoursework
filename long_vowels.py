
# Takes a string as an input and extends the vowels.

user = input("what word would you like to extend? ").lower()

vowels = "aeiou"

new_string = " "

index = 0

for i in range(len(user)):
    if user[i] == user[i - 1] and user[i] in vowels:
        new_string += user[i] * 4
    else:
        new_string += user[i]
    i += 1 
print(new_string)
    


        
