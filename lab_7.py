
#1. will the code run, and if so, what will be the data types and values of a and b?

a, b = [10, 11]
a, b = [10]
a, b = [10, 11, 12]
a, *b = [10, 11]
a, *b = [10]
a, *b = [10, 11, 12]

#2. what data type is args and kwargs inside the function, what are the values,
#and how would you use them?
def base_function(*args, **kwargs):
    print('arg: ', args)
    print('kwarg: ', kwargs)

base_function()
base_function(['A', 'B'])
base_function('Hello', 'World', '!')
base_function(answer=True, question='No')
base_function('a', 'b', c='value', d=10)


#3. write a lambda function that is passed into my_func, and performs a valid
#operation on a and b, without editing the contents of my_func at all.

def my_func(a, b, func):
    value = func(a, b)
    return value

my_func(10, 10, func = lambda a, b: sum([a, b]))

#
def sum(*ml): 
    v = 0
    for i in ml: 
        print(i)

    return v

sum([1,1])
sum(1,1)