# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:08:46 2022

@author: Cindy
"""

BASE_VAL = 100; 
def value_tester(*ab, func=sum):
    val = func(ab)
    if val > BASE_VAL: 
        statement = 'bigger than'
    elif val == BASE_VAL: 
        statement = 'the same as' 
    else: 
        statement = 'smaller than'
        
    print(f'The value is {statement} the base value.')
    
value_tester(100, 10)
a, b = [1, 2]
print(a)



# lambda function
def my_func(a, b): 
    return (a + b) / 2

lambda a, b: (a + b)/2
my_func(20, 5)
# Do not assign a name to the lambda !!

value_tester(100, 10, func = lambda ab: sum(ab) / len(ab))


# class inheritance
class Vehicle(): 
    def __init__(self, kind): 
        self.kind = kind
    def what_am_i(self): 
        print(f'I am a {self.kind}.')
    def fuel(self):
        print('I use oil for fuel.')
        
vehicle = Vehicle('car')
vehicle.what_am_i()
vehicle.fuel()

class Bicycle(Vehicle): 
    def fuel(self): 
        print('I am people-powered.')
    def peddle_me(self): 
        print('You have to peddle fast.')
bicycle = Bicycle('bicycle') 
bicycle.fuel()
bicycle.peddle_me()

class MyString(str): 
    def say_hello(self):
        print('Hello world')
    def lower(self): 
        print('I do not want to be lowercase.')
        
ms = MyString('one')
ms.say_hello()
print(ms.capitalize())
ms.lower()
print(ms.upper())