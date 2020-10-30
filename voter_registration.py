# Rob Young
# 18 OCT 2020
# voter_registration.py
# SDEV300

"""This program provides a voter registration application and confirms voter eligibility"""

# imported modules
import sys

# welcome statement and initial input
print('*********************************************************')
print('Welcome to the Python Voter Registration Application')
print('Do you want to register to vote? Please enter Yes or No: ')
choice = input('Please enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while choice == "":
    choice = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while choice not in ['YES', 'NO']:
    choice = input('Please enter valid input: ').upper()

# determines whether the application continues
if choice.upper() == 'NO':
    print('Thank you, goodbye!')
    sys.exit()

# first name input and validation
first_name = input('Please enter your first name: ')

while first_name == "":
    first_name = input('Cannot be left blank. Please enter your first name: ')

while not first_name.isalpha():
    first_name = input('Please enter a valid first name: ')

# checks for registration continuation
choice = input('Would you like to continue with registration? Please enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while choice == "":
    choice = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while choice not in ['YES', 'NO']:
    choice = input('Please enter valid input: ').upper()

# determines whether the application continues
if choice.upper() == 'NO':
    print('Thank you, goodbye!')
    sys.exit()

# last name input and validation
last_name = input('Please enter your last name: ')

while last_name =="":
    last_name = input('Cannot be left blank. Please enter your last name: ')

while not last_name.isalpha():
    last_name = input('Please enter a valid last name: ')

# checks for registration continuation
choice = input('Would you like to continue with registration? Please enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while choice == "":
    choice = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while choice not in ['YES', 'NO']:
    choice = input('Please enter valid input: ').upper()

# determines whether the application continues
if choice.upper() == 'NO':
    print('Thank you, goodbye!')
    sys.exit()

# age input and validation
age = input('Please enter your age: ')

while age == '':
    age = input('Cannot be left blank. Please enter your age: ')

while not age.isdigit():
    age = input('Please enter a valid age: ')

# checks for appropriate age range
while int(age) > 120:
    age = input('Please enter a valid age: ')

# checks to make sure registrant is at least 18
if int(age) < 18:
    print('You are not old enough to vote. Please register once you turn 18. Goodbye')
    sys.exit()

# checks for registration continuation
choice = input('Would you like to continue with registration? Please enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while choice == "":
    choice = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while choice not in ['YES', 'NO']:
    choice = input('Please enter valid input: ').upper()

# determines whether the application continues
if choice.upper() == 'NO':
    print('Thank you, goodbye!')
    sys.exit()

# US Citizenship verification
citizen = input('Are you a US citizen? Enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while citizen == "":
    citizen = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while citizen not in ['YES', 'NO']:
    citizen = input('Please enter valid input: ').upper()

# non-citizen response
if citizen.upper() == 'NO':
    print('You must be a US citizen to register to vote. Exiting registration process.')
    sys.exit()

# checks for registration continuation
choice = input('Would you like to continue with registration? Please enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while choice == "":
    choice = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while choice not in ['YES', 'NO']:
    choice = input('Please enter valid input: ').upper()

# determines whether the application continues
if choice.upper() == 'NO':
    print('Thank you, goodbye!')
    sys.exit()

# state input
state = input('Which state do you live in? Please enter postal abbreviation (ex. MD, IL): ').upper()

# checks to make sure input isn't left blank
while state == "":
    state = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure a valid state was entered
while not state.isalpha() or len(state) != 2:
    state = input('Not valid input. Please enter a valid state abbreviation: ').upper()

# checks for registration continuation
choice = input('Would you like to continue with registration? Please enter Yes or No: ').upper()

# checks to make sure input isn't left blank
while choice == "":
    choice = input('Cannot be left blank. Please enter a valid answer: ').upper()

# checks to make sure input is valid
while choice not in ['YES', 'NO']:
    choice = input('Please enter valid input: ').upper()

# determines whether the application continues
if choice.upper() == 'NO':
    print('Thank you, goodbye!')
    sys.exit()

# zip code input
zipcode = input('Please enter your zip code: ')

# checks to make sure zip code is valid
while zipcode == '':
    zipcode = input('Cannot be left blank. Please enter a valid zip code: ')

while not zipcode.isdigit():
    zipcode = input('You must enter an integer. Please enter a valid zip code: ')

while int(zipcode) > 99999 or int(zipcode) < 10000:
    zipcode = input('Please enter a valid zip code: ')
    zipcode = int(zipcode)

# final output
print('\nCongratulations! You eligible to vote!')
print('Below is the information you have entered:')
print('\nFirst Name: ', first_name)
print('Last Name: ', last_name)
print('Age: ', age)
print('US Citizen: ', citizen)
print('State: ', state)
print('Zip Code: ', zipcode)
print('\nThank you for registering to vote! Your registration card is on its way!')
