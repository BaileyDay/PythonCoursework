
# A script that asks the user for a number, and prints the corresponding day of the week.

day = int(input('Day (0-6)? '))

# Creates a list of days of the week.

days_of_the_week = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# The actual print function. 

print(days_of_the_week[day])

# A conditional statement that check to see if the value is equal to Saturday, or Sunday. It then prints the appropriate response.

if (day == 0) or (day == 6):
    print("Sleep In")
else:
    print("Go to work")