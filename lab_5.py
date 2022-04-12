#1: this code does not run!  try it and examine the errors, then figure out what needs to
#be changed to make it work

a = 10
b = 20
c = 30

def first_func(b=20):
    c = 30
    value = second_func()
    return value

def second_func(d=40):
    e = 50
    return a + b + c + d + e

result = first_func()

#2: take this code from Thursday's lab and write a function so that the form of
#the final answer is:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}
date_format = '%m/%d/%Y'
def key_func(k): 
    return k.capitalize()
def val_func(v): 
    return datetime.datetime.strptime(v, date_format).date()
answer = {key_func(k):val_func(v) for k, v in start_dict.items()}
print(answer)
