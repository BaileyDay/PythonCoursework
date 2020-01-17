
# Dictionary exercises for python

from collections import Counter

# Exercise 1 ------------------------------------------------------
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])

phonebook_dict['Kareem'] = '939-489-1234'

del phonebook_dict['Alice']

phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict)

# Exercise 2 -------------------------------------------------------

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit['email'])

print(ramit['interests'][0])

print(ramit['friends'][0]['email'])

print(ramit['friends'][1]['interests'][1])

# Letter summary --------------------------------------------------------

user = input('Please enter a word.')

letter_count = {}

for x in user:
    if x in letter_count:
        letter_count[x] += 1 
    else:
        letter_count[x] = 1

print(letter_count)

# Word Summary -----------------------------------------------------------

user1 = input('Please enter a sentence.')

user11 = user1.split(" ")

word_count = {}

for i in user11:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1 

print(word_count)

# Bonus exercise ----------------------------------------------------------

c = Counter(word_count)

highest = c.most_common(3)

print(highest)