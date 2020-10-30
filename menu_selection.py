# Rob Young
# 26 October 2020
# menu_selection.py
# SDEV300

"""
This program allows a user to make a selection from a menu and perform
the selected action
"""

# imported modules
import secrets
import string
import datetime
from datetime import date
import math
import sys

# welcome statement and initial input
print('****************************************************')
print('Welcome to my menu selection app!')
print('Here are the options you can choose from:\n')

# menu options
print('a. Generate a Secure Password')
print('b. Calculate and Format a Percentage')
print('c. How many days from today until July 4, 2025?')
print('d. Use the Law of Cosines to calculate the leg of a triangle')
print('e. Calculate the Volume of a Right Circular Cylinder')
print('f. Exit Program\n')

# user input
choice = input('Please enter one of the letters above indicating your choice: ').lower()

# validates input
while choice == '':
    choice = input('Cannot be left blank. Please select a choice from the menu above: ').lower()

while choice not in['a', 'b', 'c', 'd', 'e', 'f']:
    choice = input('Please only select a choice from the menu above: ').lower()

while not choice == 'f':
    # Choice a - Secure Password Generation
    if choice == 'a':
        print('\nGenerating a Secure Password')

        # sets password length
        length = input('How long would you like your password to be? ')

        # validates length input
        while length == '':
            length = input('Cannot be left blank. Please enter password length: ')

        while not length.isdigit():
            length = input('Please enter only integers for password length: ')

        length = int(length)

        # determines and validates makeup of password
        # upper case letters
        uc = input('Would you like to use upper case letters? Enter Yes or No: ').lower()

        while uc == '':
            uc = input('Cannot be left blank. Please enter Yes or No: ').lower()

        while uc not in ['yes', 'no']:
            uc = input('Please enter only Yes or No: ').lower()

        if uc == 'yes':
            UPPER = string.ascii_uppercase
        else:
            UPPER = ''

        # lower case letters
        lc = input('Would you like to use lower case letters? Enter Yes or No: ').lower()

        while lc == '':
            lc = input('Cannot be left blank. Please enter Yes or No: ').lower()

        while lc not in ['yes', 'no']:
            lc = input('Please enter only Yes or No: ').lower()

        if lc == 'yes':
            LOWER = string.ascii_lowercase
        else:
            LOWER = ''

        # numbers
        num = input('Would you like to use numbers in your password? Enter Yes or No: ').lower()

        while num == '':
            num = input('Cannot be left blank. Please enter Yes or No: ').lower()

        while num not in ['yes', 'no']:
            num = input('Please enter only Yes or No: ').lower()

        if num == 'yes':
            NUMBER = string.digits
        else:
            NUMBER = ''

        # special characters
        spechar = input('Would you like special chars in your password? Enter Yes or No: ').lower()

        while spechar == '':
            spechar = input('Cannot be left blank. Please Enter Yes or No: ').lower()

        while spechar not in ['yes', 'no']:
            spechar = input('Please only Yes or No: ').lower()

        if spechar == 'yes':
            SPECIAL_CHAR = string.punctuation
        else:
            SPECIAL_CHAR = ''

        def custom_pass(a_length, a_upper, a_lower, a_number, a_special):
            """function that creates a custom password from user input"""
            alphabet = a_upper + a_lower + a_number + a_special
            if alphabet == '':
                password = ''
                return password
            password = ' '.join(secrets.choice(alphabet) for i in range(a_length))
            return password

        if custom_pass(length, UPPER, LOWER, NUMBER, SPECIAL_CHAR) == '':
            print('\nCannot have blank password. Starting over...\n')
        else:
            print('\nPassword is ', custom_pass(length, UPPER, LOWER, NUMBER, SPECIAL_CHAR),'\n')

    elif choice =='b':
        # Choice b - Calculating and Formatting a percentage
        print('\nPercentage Calculation and Formatting')

        # data entry and validation - numerator
        numerator = input('Please enter an integer: ')

        while numerator == '':
            numerator = input('Cannot be left blank. Please enter an integer: ')

        while not numerator.isdigit():
            numerator = input('Please enter integers only: ')

        # data entry and validation - denominator
        denominator = input('Please enter a second integer: ')

        while denominator == '':
            denominator = input('Cannot be left blank. Please enter an integer: ')

        while not denominator.isdigit():
            denominator = input('Please enter integers only: ')

        # data entry and validation - decimal places
        dec = input('Please enter a third integer: ')

        while dec == '':
            dec = input('Cannot be left blank. Please enter an integer: ')

        while not dec.isdigit():
            dec = input('Please enter integers only: ')

        numerator = int(numerator)
        denominator = int(denominator)
        dec = int(dec)

        def percentage(a_numerator, a_denominator, a_dec):
            """function that calculates and formats percentage from user input"""
            quotient = (a_numerator / a_denominator) * 100
            output = ('{:.{}f}'.format(quotient, a_dec))
            return output

        print('\n',percentage(numerator, denominator, dec),'%\n')

    elif choice == 'c':
        # choice c - how many days until July 4, 2025
        print('\nHow many days from today until July 4, 2025?')

        today = date.today()
        target_date = datetime.date(2025, 7, 4)
        time_to_date = abs(target_date - today)
        print('\n',time_to_date.days, 'days until July 4, 2025\n')

    elif choice == 'd':
        # choice d - using law of cosines to calculate leg of triangle
        print('\nCalculating the leg of a triangle with law of cosines')

        # leg 1 data entry and validation
        leg1 = input('Please enter the length of the first leg: ')

        while leg1 == '':
            leg1 = input('Cannot be left blank. Please enter length of first leg: ')

        while not leg1.isdigit():
            leg1 = input('Please enter integers only: ')

        # leg 2 data entry and validation
        leg2 = input('Please enter the length of the second leg: ')

        while leg2 == '':
            leg2 = input('Cannot be left blank. Please enter length of second leg: ')

        while not leg2.isdigit():
            leg2 = input('Please enter integers only: ')

        # angle data input and validation
        angle1 = input('Please enter the angle measurement: ')

        while angle1 == '':
            angle1 = input('Cannot be left blank. Please enter angle: ')

        while not angle1.isdigit():
            angle1 = input('Please enter integers only: ')

        leg1 = int(leg1)
        leg2 = int(leg2)
        angle1 = int(angle1)

        def law_of_cosines(a_leg, b_leg, a_angle):
            """function that calculates leg of a triangle"""
            cos = ((a_leg ** 2) + (b_leg ** 2))
            radians = math.radians(a_angle)
            result = cos - (2 * a_leg * b_leg * math.cos(radians))
            return math.sqrt(result)

        print('\nLength of leg is ', law_of_cosines(leg1, leg2, angle1),'\n')

    elif choice == 'e':
        # choice e - calculating volume of right circular cylinder
        print('\nCalculating the Volume of a Right Circular Cylinder')

        # radius data entry and validation
        radius = input('Please enter the radius of the base: ')

        while radius == '':
            radius = input('Cannot be left blank. Please enter radius: ')

        while not radius.isdigit():
            radius = input('Please enter integers only: ')

        # height data entry and validation
        height = input('Please enter the height of the cylinder: ')

        while height == '':
            height = input('Cannot be left blank. Please enter height: ')

        while not height.isdigit():
            height = input('Please enter integers only: ')

        radius = int(radius)
        height = int(height)

        def right_circular_cylinder_vol(a_rad, b_hei):
            """function that calculates volume of right circular cylinder"""
            volume = (a_rad ** 2) * b_hei
            return math.pi * volume

        print('\nVolume of cylinder is ', right_circular_cylinder_vol(radius, height),'\n')

    choice = input('Please make another choice from the menu above: ').lower()

    # edits program when menu choice = 'f'
    if choice == 'f':
        print('Thank you for using my application! Goodbye!')
        sys.exit()
