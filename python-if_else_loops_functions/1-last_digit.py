#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
    mod = number % -10

if number % 10 == 0:
    print(f'Last digit of {number} is 0 and is 0')
elif number % 10 < 6:
    print(f'Last digit of {number} is {mod} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {mod} and is greater than 5')
