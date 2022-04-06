# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:12:20 2022

@author: Cindy
"""

# boolean
val1 = True
# T must be capitalized. 
val2 = 10 < 100
print(val1)
print(val2)

my_list = ['a', 'b', 'c', 'd']
val1 = 'a' in my_list
val2 = 'z' not in my_list
print(val1)
print(val2)

my_string = 'Hello world!'
val1 = my_string.startswith('H')
val2 = not my_string.isnumeric()
print(val1)
print(val2)

# logic
x = 10
y = 100
z = 'No'
val1 = (x > y) or (x ==y and y != 101 and (y+1 ==101 or z =='No'))
print(val1)

# the 'if' statement block
x = 10
if x == 11:
    print('This number is big.')
elif x >100:
    print('Whoa, huge number.')
elif x == 0:
    print('Basically no number.')
else:
    print('What happened')


# 'For' Loops
my_list = ['a', 'b', 'c', 'd']
for letter in my_list:
    print('The letter is :', letter)
    
for i in range(5):
    print('in the loop.')
print('Not in the loop')

# combining 'if' statement and 'For' loop
my_list = ['a', 'b', 'c', 'd']
for letter in my_list:
    if letter == 'c':
        print('I see the c.')
    else:
        print('Not it..')
        
# break: Immediately exits the current loop
my_list = ['a', 'b', 'c', 'd']
for letter in my_list:
    if letter == 'c':
        print('I see the c.')
        break
    else:
        print('Not it..')
        
# continue: Immediately goes to the next itertion of the current loop. 
my_list = ['a', 'b', 'c', 'd', 'e']
for letter in my_list:
    if letter == 'c':
        continue
    else:
        print('I see the', letter)
    print('Done with that iteration...')
print('Where did the "c" go??')
        
# the 'while' loop
x = 0
while x < 5: 
    print('x is', x)
    x+=1
    
# list comprehensions
# [f(v) for v in starting_list]
# [f(v) for v in starting_list if <condition>]

# mapping
letters = ['a', 'b', 'c', 'd', 'e']
mapped = [l.upper() for l in letters]
print(mapped)

# filtering
filtered = [l for l in letters if l != 'c']
print(filtered)
    
# mapping and filtering
mapped_and_filtered = [l.upper() for l in letters if l != 'c']
print(mapped_and_filtered)

# Iterating over dictionaries
my_dict = {'a':100, 'b':200, 'c':300, 'd':400}
for key in my_dict.keys():
    print('First key:', key)
    
for val in my_dict.values():
    print('First value:', val)

# interlude: unpacking notation
x, y = [10, 20]
print(x)
print(y)

# Iterating over dictionaries
for items in my_dict.items():
    print(items)

for key, val in my_dict.items(): 
    print('First key:', key)
    print('First value:', val)

# Dictionaly comprehensions
# {f(key):f(val) for key, val in my_dict.items()}
my_dict = {'a':100, 'b':200, 'c':300, 'd':400}
new_dict = {key:val*2 for key, val in my_dict.items()}
print(new_dict)

start_list = ['a', 'b', 'c', 'd', 'e']
new_dict = {key.upper():None for key in start_list}
print(new_dict)
# {'A': None, 'B': None, 'C': None, 'D': None, 'E': None}











