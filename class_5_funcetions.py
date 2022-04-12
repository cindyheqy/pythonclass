# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:26:52 2022

@author: Cindy
"""
def my_func(num):
    new_num = (num * 2 + 40) / 10
    return new_num

value = my_func(10)
print(value)

value = my_func(11)
print(value)

def my_func(num, denominator=10): 
    new_num = (num * 2 + 40) / denominator
    return new_num

value = my_func(10)
print(value)

value = my_func(10, denominator = 100)
print(value)

#functions and name-space
my_global = 10
def my_func(): 
    my_local = 20
    return my_local * my_global

print(my_func())
print(my_global)
print(my_local)


# functions: an example

names_2021 = [' jeff', 'molly', 'YIJIA', 'Jon', 'RaHuL', 'noah', 'Bob']
names_2021 = [n.strip().capitalize() for n in names_2021]
print(names_2021)

fixed_names = []
for n in names_2021: 
    if n =='Jon': 
        result = 'John'
    elif n =='Bob':
        result = 'Bob does not work here any more!'
    else: 
        result = n
    fixed_names.append(result)
print(fixed_names)

names_2020 = ['JEFF', ' sarah', 'Simo n', 'Sawyer']
names_2020 = [n.strip().capitalize() for n in names_2020]
print(names_2020)

new_fixed_names = []
for n in names_2020: 
    if n == 'Simo n': 
        result = 'Simon'
    else: 
        result = n
    new_fixed_names.append(result)
print(new_fixed_names)


def name_fixer(n): 
    n = n.strip().capitalize()
    if n =='Jon': 
        result = 'John'
    elif n == 'Bob': 
        result = 'Bob does not work here any more!'
    elif n == 'Simo n': 
        result = 'Simon'
    else: 
        result = n
    return result
    
fixed_names = [name_fixer(n) for n in names_2021]
print(fixed_names)
new_fixed_names = [name_fixer(n) for n in names_2020]
print(new_fixed_names)
