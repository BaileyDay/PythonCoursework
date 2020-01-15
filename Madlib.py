# Allows the sleep function.

import time

# A simple Madlibs game that prompts the user for different subjects and prints a sentence. 

print("Welcome to Madlibs! Please answer the following questions, Thanks!")

time.sleep(2)

# Variables

color = str(input("What is your favorite color? "))

location = str(input("Where are you from? "))

name = str(input("What is your name? "))

age = str(input("How old are you? "))

food = str(input("what is your favorite food? "))

# Start of the string cocantenation

print("Thanks for answering")

time.sleep(1)

print("Now computing your custom sentence!")

time.sleep(1.5)

print("...")

time.sleep(1.5)

print("...")

time.sleep(1.5)

print("...")

time.sleep(1.5)

# Finished string

print("{}, is {} years old! They are from {}! Their favorite food is {} {}, weird!!".format(name, age, location, color, food))



