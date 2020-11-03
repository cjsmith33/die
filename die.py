"""
A simple die roller

Author: Charles Smith
Date: November 01, 2020
"""
import random
first = input('Type the first number: ')
first = int(first)
last = input('Type the last number: ')
last = int(last)
print('Choosing a number between ' + str(first) + ' and ' + str(last) + '.')
roll = random.randint(first,last)
print('The number is ' + str(roll) + '.')
