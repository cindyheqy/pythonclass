# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:24:00 2022

@author: Cindy
"""

# assert
x = 10
y = 0
assert(y != 0), 'Error: y cannot be 0'
z = x / y


# try except
x = 10
y = [0]
try: 
    z = x / y
except ZeroDivisionError: 
    print('Error: y cannot be 0')
except IndexError: 
    print('Error: the length of list y is not correct')
except:
    print('Something else went wrong...')


# isinstance
isinstance('Hello world', str)
isinstance('Hello world', int)

def string_fixer(s): 
    assert(isinstance(s, str)), 'string_fixer requires string arg'
    s = s.lower().strip()
    print(s)
    if s.startswith('a'):
        return "it's an a!"
    else: 
        return "it's not an a."

string_fixer(42)


# isinstance with number
import numbers
def math_some_numbers(a, b): 
    assert(isinstance(a, numbers.Number) and 
           isinstance(b, numbers.Number)), 'Must pass in numeric arguments!'
    val = (a + b) * 2
    return val