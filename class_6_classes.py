# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:33:17 2022

@author: Cindy
"""
a = 10

def func_one(b=20): 
  c = 30
  def func_two(d=40): 
    e = 50
def func_three(f=60): 
  g = 70
  
  
class Myclass(): 
    a = 10
    b = 20
    x = a + b
    
mc_instance = Myclass()

mc_instance.x

my_string = str()
my_string

class MyClass(): 
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b
        
        
class HouseValues(): 
    def __init__(self, num_bedrooms, num_baths, sqrt):
        # needs three values: num bedrooms, num bathrooms, sqft
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft
    def estimate_value(self): 
        # use an equation of questionable accuracy that I found on a random
        # website to estimate the value based on those three parameters
        bedroom_mod = (())
    def pick_a_neighborhood(self): 
        # randomly pick a modifier to multiple the value estimate by
        pass