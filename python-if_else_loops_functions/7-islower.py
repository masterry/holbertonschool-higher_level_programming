#!/usr/bin/python3
if letter < 123 and letter > 97:
    print("{:c} is lower".format(letter))
elif letter < 91 and letter > 65:
    print("{:c} is upper".format(letter))      
else:
    print("{:d} is upper".format(letter))
