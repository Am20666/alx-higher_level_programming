#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for r in my_string:
        if r != 'c' and r != 'C':
            new_string += r
    return new_string
