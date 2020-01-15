
# A script that lets a user determine the total amount to tip based on input. 


# Levels of service variables 

good = 0.20

fair = 0.15

bad = 0.10


# Beggining of input

check = float(input("What was the total before tip? "))
service = input("How was the service? Good? Fair? or Bad? ").lower()
people = int(input("How many people does it need to be split between?"))


# Beginning of conditions

if service == "good":
    print("The total per person is " + str(((check * good) + check) / people))
elif service == "fair": 
    print("The total per person is " + str(((check * fair) + check) / people))
elif service == "bad":
    print("The total per person is " + str(((check * bad) + check) / people))
else: 
    print("you didnt select a valid service ")
