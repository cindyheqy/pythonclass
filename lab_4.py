#convert these objects!

#1
start_list = [[2, 3, 4], [6, 8, 9]]
l = []
#turn it into [1,    2,   3, 4   ]

# my answer
for n in start_list:
    for i in range(len(n)):
        if n[i] % 2 == 0:
            l.append(n[i]/2)
print(l)
        
# correct answer
start_list = [[2, 3, 4], [6, 8, 9]] 
[item for sublist in start_list for item in sublist if item % 2 ==0]



#2
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'zach': datetime(2005, 8, 8)}

date_format = '%m/%d/%Y'
answer = {k.capitalize():datetime.datetime.strptime(v, date_format) for k, v in start_dict.items()}
# refer to the end of the lecture slides for more on dictionary comps