
# Person class for first exercise.

class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0
         self.met = []
         self.num_unique_people_greeted = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person not in self.met:
            self.met.append(other_person)
            self.num_unique_people_greeted += 1




    def contactinfo (self):
        print(self.email + " " + self.phone)

    def add_friend(self, friend):
        self.friends.append(friend.name)
    
    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)



# Beggining of first exercise

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# Calling the greet method

sonny.greet(jordan)

jordan.greet(sonny)

# Calling a newly created method that prints their contact info.

sonny.contactinfo()

jordan.contactinfo()

# Appending friends to the empty friends list that was created in the __init__

jordan.add_friend(sonny)

sonny.add_friend(jordan)

# Checking to see if the friend was properly appended to the new list.

sonny.num_friends()
print(sonny.friends)

# Exercise 2, make your own class.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.make + " " + self.model + " " + str(self.year))




car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()