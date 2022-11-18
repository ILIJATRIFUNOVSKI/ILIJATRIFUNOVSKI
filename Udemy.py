# Formating Strings
num = 12
name = 'Ile'
print('My number is {} and my name is {}. '.format(num, name))  #1way
print('My number is {one} and my name is {two} more {one}'.format(one=num, two=name))  #2way
# Indexing strings
s='Hello'
print(s[0])
#slicing notation
print(s[0:])
print(s[:3]) #bez 3 printa
print(s[0:3])
#   LISTS
my_list=['a','b','c']
my_list.append('d') #adding new element
print(my_list[0])   #getting first element
print(my_list[1:3])
my_list[0] = 'NEW'  #reasign new element replace
print(my_list)
nest=[1,2,[3,4]]    #nested list list inside a list
print(nest[2][1]) #getting the number 4 [second list is index no2]
nest=[1,2,3,[4,5,['target']]] #grab target
print(nest[3])  #[4, 5, ['target']]
print(nest[3][2])   #['target']
print(nest[3][2][0])    #0 for only element target
    # DICTIONARIES
d = {'key1':'value', 'key2':123}
print(d['key1'])
d = {'k1' : [1, 2, 3]}
print(d['k1'][1])
d = {'k1':{'innerkey':[1,2,3]}} #nested dictionary
print(d['k1']['innerkey'][1])
    # BOOLEANS True False
    # TUPLES
t = (1, 2, 3)
print(t[0])
#t[0]="NEW" Tuples are immutable not like lists mutable
    # SETS
s = {1, 1, 2, 2, 3, 3 ,3}
print(s)    # returns {1, 2, 3} does not support duplicate
list0 = [1,1,1,5,5,5,7,8,9,9,9]
print(set(list0))   #making a sef out of list
s.add(5)    #addding a new element
    # COMPARISON OPERATORS
#True False 1>2 1<2 1>=2 1<=2 1==2 you must do 2== if one python thinks we make variable assign
# 1=!3 'hi'=='bye'

#a<b and b<a With AND operator all conditions must be True
# OR at least one condition must be true True or False returns True
    #IF ELIF ELSE Statements
if 1<2:
    print('yep')

if 1 == 2:
    print('first')
elif 4 == 4:    #it executes only the first true condition
    print('second')
elif 3 == 3:
    print('middle')
else:
    print('last')
    # FOR LOOPS (allow to loop trough sequence)
seq=[1, 2, 3, 4, 5]
for item in seq:
    print(item)
for num in seq:
    print('Hello')
    # WHILE LOOP
i=1
while i < 5:
    print('i is: {}'.format(i))
    i+=1    #i=i+1
    #RANGE
for x in range(0,5):
    print(x)
print(list(range(0,5))) #if we want a list (START,STOP,STEP)
    # LIST COMPREHENSION is like for loop but backwards
x=[1, 2, 3, 4]
#out = []
#for num in x:
#    out.append(num**2)
#print(out)
print([num**2 for num in x])    #this is list comprehension
#out=[num**2 for num in x]
    # FUNCTIONS
def my_func(param1):
    print(param1)
my_func('hello')

def my_func(name='Default name'):
    print('Hello '+name)    #printing
my_func()
my_func('Ilija')

def square(num):
    """
    THIS IS A DOCSTRING
    CAN GO MULTIPLE LINES.
    THIS FUNCTION SQUARES A NUMBER
    """
    return num**2   #returning
output=square(2)
print(output)
#square with typing this and shift tab you see the """ text
    # LAMBDA EXPRESSIONS using mapping filter
    #map() function
#def times2(var):
#    return var*2
#def times2(var):return var*2 #replacement for 107 and 108
t=lambda var:var*2
#print(t(6))
#x=times2(5)
print(x)

seq=[1, 2, 3, 4, 5]
#print(list(map(times2,seq)))
#print(times2)
print(list(map(lambda num: num*3,seq)))
    # FILTER function
print(list(filter(lambda num:num%2==0,seq)))    #num%2==0 is like bool func
    # METHODS
s='hello my name is Ilija'
print(s.lower()) #with s. we have many methods
print(s.upper())
print(s.split())
tweet='Go Sports! #Sports'
print(tweet.split())
print(tweet.split('#'))
print(tweet.split('#')[1])
d = {'k1': 1, 'k2': 2}
print(d.keys()) #same with dict. dictname.(and we have methods)
print(d.items())
print(d.values())
lst = [1, 2, 3, 4, 5]
#print(lst.pop())
item = lst.pop()
print(item)
first = lst.pop(0)  #1st index is popped
print(lst)
print(first)
lst.append('new')
print(lst)
    # IN operator (for checking if something is inside)
print('x' in [1, 2, 3])
print('x'in ['x','y','z'])
    # Tuple unpacking
x=[(1,2),(3,4),(5,6)]
print(x[0][1])
for item in x:  #this is Tuple unpacking
    print(item)
for a,b in x:
    print(a)    #output 1,3,5 if b will print second item in this tuples
    print(b)    # if both pring output is 123456



