#### fix the following errors!

x = min(10, 1, 0, 100)
print(x)

print(set([1, 2, 1]))
print(list('abc'))
print(dict(a=1, b=2))

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[-1])

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z.append('d')
z[2] = 'd'
print(z)

#5 why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
color = 'My favorite color is %s, what is yours?' % 'blue'
print(color)

#### answer the following questions without changing the code given

#7 make the entries in this list unique
schools = {'harris', 'booth', 'crown', 'harris', 'harris'}

#8 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals2=list(animals)
animals2[2]='cat'
print(animals2)

#9 make this string take a name based on a variable (you can modify the code on this one)
name = 'Sarah'
welcome = f'Hello {name}, and welcome to Data and Programming!'
print(welcome)

#10 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
# my_sent.lower().split()
lower_sent = my_sent.lower()
print(lower_sent.split())