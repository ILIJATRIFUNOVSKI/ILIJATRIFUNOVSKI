#print("HelloWorld")
#x=4
#x="Ilija"
#print(x)

#x=str(3)
#y=int(3)
#z=float(3)
#print(x,y,z)
#print(type(x))
#x,y,z="Orange","Apple","Banana"
#print(x)
#print(y)
#print(z)

#x=y=z="Orange"
#print(x)
#print(y)
    #Unpacking a list
#fruits=["apple","banana","cherry"]
#x,y,z=fruits
#print(x)
#print(y)
#print(z)
    #GLOBAL Variables and LOCAL Variables
#x="awesome"
#def myfunc():
    #global x   #To make a global function or to change global variable value
#    x="fantastic"
#    print("Python is "+x)   #LOCAL
#myfunc()
#print("Python is "+x)   #GLOBAL
    #DATA TYPES
#x = "Hello World"	#str
#x = 20	#int
#x = 20.5	#float
#x = 1j	#complex
#x = ["apple", "banana", "cherry"]	#list
#x = ("apple", "banana", "cherry")	#tuple
#x = range(6)	#range
#x = {"name" : "John", "age" : 36}	#dict
#x = {"apple", "banana", "cherry"}	#set
#x = frozenset({"apple", "banana", "cherry"})	#frozenset
#x = True	#bool
#x = b"Hello"	#bytes
#x = bytearray(5)	#bytearray
#x = memoryview(bytes(5))	#memoryview

    #SPECIFING DATA TYPE
#x = str("Hello World")	str
#x = int(20)	int
#x = float(20.5)	float
#x = complex(1j)

    #NUMBER TYPE CONVERSION
#x=1
#y=2.8
#z=1j
#a=float(x)
#b=int(y)
#c=complex(x)
#print(a,b,c)
#print(type(c))
    #RANDOM built in module
#import random
#print(random.randrange(1,10))

    #STRINGS

#Looping through a String
#for x in "banana":
#    print(x)
#print(len(x)) #determing the length of characters

    #check string "in","not in "

#txt="The best things in life are free!"
#print("free"in txt)

#if "free" in txt:
#    print("Yes, 'free' is present.")

#print("expencive" not in txt)
#if "expencive" not in txt:
#    print("No, 'expencive' is NOT present.")

    #SLICING STRINGS

#b="Hello World!"
#print(b[2:5]) #from position 2 to position5(not included)
#print(b[:5]) #from start position
#print(b[2:]) #from 2position to the end
#print(b[-5:-2]) #negative indexing
    #Modifying strings
#print(b.upper())
#print(b.lower())

#a=" Hello, World! "
#print(a.strip())    #"Hello, World!" without white space
#print(a.replace("H","j"))   #replacing strings
#print(a.split(",")) #spliting words with comma ['Hello', ' World!']
    #Concatenate strings "+"
#a="Ilija"
#b="Trifunovski"
#c=a +" "+ b
#print(c)
    #Format Strings
#age=27
#txt="My name is Ilija,and i am {}"
#print(txt.format(age))

#quantity=3
#itemno=567
#price=50.56
#myorder="I want to pay {2} dollars for {0} pieces of item {1}."
#print(myorder.format(quantity,itemno,price))
    #Escape character
#txt="We are so called \"Vikings\" from the north."
#print(txt)
#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value
    #String Methods
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning

    #BOOLEANS
#a=200
#b=33
#if b > a:
#    print("b is greater than a")
#else:
#    print("b is not greater than a")

#class myclass():
#    def __len__(self):
#        return 0
#myobj=myclass()
#print(bool(myobj))

#x=200
#print(isinstance(x,int))    #isinstance to check an object if int or not

    #PYTHON OPERATORS

    #Arithmetic Operators
#+	Addition	x + y
#-	Subtraction	x - y
#*	Multiplication	x * y
#/	Division	x / y
#%	Modulus	x % y
#**	Exponentiation	x ** y
#//	Floor division	x // y

    #Assignment Operators (to assign values to variables)
#=	x = 5	x = 5
#+=	x += 3	x = x + 3
#-=	x -= 3	x = x - 3
#*=	x *= 3	x = x * 3
#/=	x /= 3	x = x / 3
#%=	x %= 3	x = x % 3
#//=	x //= 3	x = x // 3
#**=	x **= 3	x = x ** 3
#&=	x &= 3	x = x & 3
#|=	x |= 3	x = x | 3
#^=	x ^= 3	x = x ^ 3
#>>=	x >>= 3	x = x >> 3
#<<=	x <<= 3	x = x << 3

    #Comparison Operators
#==	Equal	x == y
#!=	Not equal	x != y
#>	Greater than	x > y
#<	Less than	x < y
#>=	Greater than or equal to	x >= y
#<=	Less than or equal to	x <= y

    #Logical Operators
#and 	Returns True if both statements are true	x < 5 and  x < 10
#or	Returns True if one of the statements is true	x < 5 or x < 4
#not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

    #Identity Operators
#is 	Returns True if both variables are the same object	x is y
#is not	Returns True if both variables are not the same object	x is not y

    #Membership Operators
#in 	Returns True if a sequence with the specified value is present in the object	x in y
#not in	Returns True if a sequence with the specified value is not present in the object	x not in y

    #Bitwise Operators (used to compate binary numbers)
#& 	AND	Sets each bit to 1 if both bits are 1
#|	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
#~ 	NOT	Inverts all the bits
#<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

    #PYTHON LISTS

#indexing lists
#thislists=["apple","banana","cherry"]  #MAIN LIST FOR ALL PROGRAMS ABOVE
#print(thislists[1])
#print(thislists[-1])
#if "apple" in thislists:
#    print("Yes, 'apple' is in the fruits list")
#thislists[1]="mango"    #changing the value
#print(thislists)
#thislists[1:3]=["dragonfruit","watermelon"] #changing range of item values
#print(thislists)
# insert method
#thislists.insert(2,"pomegranate")
#print(thislists)
# adding at the end of the list
#thislists.append("gojiberry")
#print(thislists)
# insert() method to insert to a specific index
#thislists.insert(1,"blackberry")
#print(thislists)
# extend() method to add elements from another list to the current list
#listoffruits=["mangos","oranges","watermelons"]
#thislists.extend(listoffruits)
#print(thislists)
# extend() method can add lists,tuples,sets,dictionaries etc.
#thistuple=("green apple","yellow apple")
#thislists.extend(thistuple)
#print(thislists)
# remove() method
#thislists.remove("banana")
#print(thislists)
# pop() method for removing specified index(if you do not specify pop removes the last index)
#thislists.pop(1)
#print(thislists)
# del keyword also removes specified index
#del thislists[0]
#del thislists # to remove completely the whole list
# clear method empties the list(list remains but has no content)
#thislists.clear()

# FOR LOOP
#for x in thislists:
#    print(x)
# loop trough the index numbers range(),len()
#for i in range(len(thislists)):
#    print(thislists[i])
# WHILE LOOP
#i=0
#while i <len(thislists):
#    print(thislists[i])
#    i=i+1
#Looping using list comprehension
#[print(x) for x in thislists]

#newlist=[]
#for x in thislists:
#    if "a" in x:
#        newlist.append(x)
#print(newlist)
# With comprehension
#newlist=[x for x in thislists if "a" in x]
#print(newlist)

#newlist=[x for x in thislists if x !="apple"]
#print(newlist)
#newlist=[x for x in thislists]  # with no if statement
#newlist=[x for x in range(10)]  #iterable
#print(newlist)
    #expression
#newlist=[x.upper() for x in thislists]
#newlist=['hello ' for x in thislists]
#newlist=[x if x != "banana" else "orange" for x in thislists] #return if it's not banana if it is return orange.
#print(newlist)
# sorth() for sorthing lists alphanumerically,ascending
#thislists.sort()
# sorthing descnding reverse=True
#thislists.sort(reverse=True)
#print(thislists)
#numb=[100,50,65,82,23]
#numb.sort(reverse=True)
#print(numb)
# sorthing key=function (sorthing to the lowest number first)
#def myfunc(n):
#    return abs(n-50)
#numb=[100,50,65,82,23]
#numb.sort(key=myfunc)
#print(numb)
# case insensitive sorting str.lower
#thislists.sort(key=str.lower)
# reverse order
#thislists.reverse()
#print(thislists)
# Copy Lists
#mylist=thislists.copy()     # 1Method copy()
#mylist=list(thislists)      # 2Method list()
#   Join Lists
#list3=thislists+numb    # +operator

#list1=["a","b","c"]     # .append()
#list2=[1,2,3]
#for x in list2:
#    list1.append(x)
#print(list1)

#list1.extend(list2)     # extend() to add elements from one to another list
#print(list1)
# LIST METHODS
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

    # TUPLES

#thistuple=tuple(("apple","banana","cherry","orange","apple","kiwi"))    # tuple() constructor
#print(thistuple)
# acess tuple by index number
#print(thistuple[-1])
#print(thistuple[-4:-1])   #range of indexes
# check if item in tuple exists in() keyword
#if "apple" in thistuple:
#    print("Yes, 'apple' is in the fruits tuple.")
# Change Tuple Values,Add,Remove (convert to a list and then change it,and back in a tuple)
#y=list(thistuple)
#y[1]="pomegranate"
#y.append("lemon")
#y.remove("cherry")
#thistuple=tuple(y)
#print(thistuple)
#Add Tuple to a Tuple
#z=("watermelon",)
#thistuple+=z
#print(thistuple)

#del thistuple
#print(thistuple) #it will raise and error because tuple no longer exists
#   Unpacking Tuples
#fruits=("apple","banana","cherry")
#(green,yellow,*red)=thistuple # Asterisk * if num of variables < num of values
#print(green)
#print(yellow)
#print(red)
# Looping Tuples
#for x in thistuple:
#    print(x)
#for i in range(len(thistuple)):
#    print(thistuple[i])

#i=0
#while i < len(thistuple):
#    print(thistuple[i])
#    i=i+1
#Join Tuples
#thistuple2=(1,2,3)
#thistuple3 = thistuple + thistuple2 #1way
#print(thistuple + thistuple2) #2way
#thistuple4=thistuple*   # Multiply
# Tuple Methods
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found

    # SETS

#thisset={"apple","banana","orange"}
#for x in thisset:
#    print(x)
#print("banana" in thisset)  #check if banana is in thisset
# Adding items with add() method
#thisset.add("cherry")
# Ading items from another to the first set
#tropical={"pineaple","mango","papaya"}
#thisset.update(tropical)
# Adding other iterable objects(lists,tuples,dictionaries etc.)
#mylist=["kiwi","pomegranate"]
#thisset.update(mylist)
#print(thisset)
# Removing sets with remove() and discard() methods
#thisset.remove("banana")
# pop() method
#x=thisset.pop()
#print(x) #returned value is the removed item
#print(thisset)

#thisset.clear() #this method empties the set
#del thisset #this keyword will delete the set completely
    #Loop Sets
#for x in thisset:
#    print(x)
    # Join Sets union() update() methods
#set1={"a","b","c"}
#set2={1,2,3}
#set3=set1.union(set2)
#print(set3)

#set1.update(set2)
#print(set1)
    #intersection_update() method
#x={"apple","banana","cherry"}
#y={"google","microsoft","apple"}
#x.intersection_update(y)
#print(x)
    #intersection() method
#z=x.intersection(y)
#print(z)
    #symmetric_difference_update() method
#x.symmetric_difference_update(y)
    #symmetric_difference() method
#z=x.symmetric_difference(y)
#print(z)
#   SET Methods
#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two other sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with the union of this set and others

 # DICTIONARIES

#thisdict={
#    "brand":"Ford",
#    "model":"Mustang",
#    "year":1964
#}
# Acess
#x=thisdict["model"]
#x=thisdict.get("model")

#x=thisdict.keys()
#x=thisdict.values()
#print(x)
# Adding new item
#thisdict["color"]="red"
#print(thisdict)
#x=thisdict.items()
#print(x)
# Checking if some key is present in dict with in keyword
#if "model" in thisdict:
#    print("Yes, 'model' is one of the keys in the thisdict dictionary.")
# Changing Values
#thisdict["year"]=2018
#thisdict.update({"year":2020}) #you can also add with this method
# Adding Items
#thisdict["color"]="red"
# Removing items
#thisdict.pop("model")
#del thisdict["model"]
#del thisdict # for deleting whole dict.
#thisdict.clear() # empties the dict.
    # LOOPING DICTIONARIES
#for x in thisdict:  #print all KEY NAMES in the dict. one by one
#    print(x)

#for x in thisdict:
#    print(thisdict[x])  # print all Values in dict.

#for x in thisdict.values():  #returns Values of the dict.
#    print(x)

#for x in thisdict.keys():    #returns Keys of the dict.
#    print(x)

#for x, y in thisdict.items(): # loop trough both keys and values with items() method
#    print(x,y)
# Copying Dictionaries
#mydict=thisdict.copy()
#mydict=dict(thisdict)
#print(mydict)
# Nested Dictionaries
#myfamily = {
#  "child1" : {
#    "name" : "Emil",
#    "year" : 2004
#  },
#  "child2" : {
#    "name" : "Tobias",
#    "year" : 2007
#  },
#  "child3" : {
#    "name" : "Linus",
#    "year" : 2011
#  }
#}
#print(myfamily)
#creating 3 dict. than creating 1 that will contain all three dict.
#child1 = {
#  "name" : "Emil",
#  "year" : 2004
#}
#child2 = {
#  "name" : "Tobias",
#  "year" : 2007
#}
#child3 = {
#  "name" : "Linus",
#  "year" : 2011
#}

#myfamily1 = {
#  "child1" : child1,
#  "child2" : child2,
#  "child3" : child3
#}
#print(myfamily1)
# Dictionary Methods
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

    # Python Conditions IF...Else Statements

#a=33    # a and b are variables part of if condition
#b=200
#if b>a:
#    print("b is greater than a")
#elif a==b:
#    print("a and b are equal")
#else:
#    print("a is greater than b")
# short hand if for only one condition
#if a>b:print("a is greater than b")
#executing one statement one for if one for else
#a=2
#b=330
#print("A") if a>b else print("B")
#multiple else statements in one line
#a=330
#b=330
#print("A") if a>b else print("=") if a==b else print("B")
# AND logical operator used to combine conditional statements
#a=220
#b=33
#c=500
#if a>b and c>a:
#    print("Both statements are True")
# OR logical operator used to combine conditional statements
#if a>b or a>c:
#    print("At least one of the conditions is True")
# nested IF statement
#x=41
#if x>10:
#    print("Above ten,")
#    if x>20:
#        print("and also above 20!")
#    else:
#        print("but not above20.")
    #Pass
#a=33
#b=200
#if b>a:
#    pass

    # WHILE Loops
#print i as long i is less than 6
#i=1
#while i<6:
#    print(i)
#    i+=1
#exit the loop when i is 3
#i=1
#while i<6:
#    print(i)
#    if i==3:
#        break
#    i+=1
#continue the next iteration if i is 3
#i=0
#while i<6:
#    i+=1
#    if i==3:
#        continue
#    print(i)
#print a message once the condition is false
#i=1
#while i<6:
#    print(i)
#    i+=1
#else:
#    print("i is no longer less than 6")

    # FOR Loops

#print each fruit in a fruit list
#fruits=["apple","banana","cherry"]
#for x in fruits:
#    print(x)
#for x in "banana":  #looping trough a string
#    print(x)
#exit the loop when x is banana
#for x in fruits:
#    print(x)
#    if x=="banana":
#        break
#exit the loop when x is banana but break comes before print
#for x in fruits:
#    if x=="banana":
#        break
#    print(x)
#do not print banana
#for x in fruits:
#    if x=="banana":
#        continue
#    print(x)
#range() start,stop,step
#for x in range(2,30,3):
#    print(x)
#else
#for x in range(6):
    #if x==3:   loop stops at 2
     #   break
#    print(x)
#else:
#    print("Finally finished!")
#Nested Loop(The inner loop will be executed one time for each iteration of the outer loop)
#adj=["red","big","tasty"]
#fruits=["apple","banana","cherry"]
#for x in adj:
#    for y in fruits:
#        print(x,y)

    # PYTHON FUNCTIONS

#def my_function(fname): #fname is argument
#    print(fname+" Refsnes")
#my_function("Emil")
#my_function("Tobias")
#my_function("Linus")

#def my_func(fname, lname):  #Parameter
#    print(fname+" "+lname)
#my_func("Ilija","Trifunovski")  #Argument

#def my_func2(*kids):    #*if we dont know how many arguments will be passed
#    print("The youngest child is "+kids[2])
#my_func2("Emily","Tobias","Elon")
#Keyword arguments
#def my_funct3(child3,child2,child1):
#    print("The youngest kid is "+child3)
#my_funct3(child1="Emily",child2="Ilija",child3="Elias")
#Arbitary keyword arguments **kwargs
#def my_funct(**kid):    #if you dont know wo many keyword arguments will be passed into the function
#    print("His last name is "+kid["lname"])
#my_funct(fname="Ilija",lname="Trifunovski")
#Default Parameter Value
#def my_funct(country="Norway"):
#    print("I am from "+country)
#my_funct("Sweden")
#my_funct("Macedonia")
#my_funct()
#Passing a List as an argument (it would be sent the same as list)
#def my_function(food):
#    for x in food:
#        print(x)
#fruits=["Apple","Banana","Cherry"]
#my_function(fruits)
#Return values
#def my_function(x):
#    return 5*x
#print(my_function(3))
#print(my_function(5))
#print(my_function(8))
#Recursion
#def tri_recursion(k):
#    if(k>0):
#        result=k+tri_recursion(k-1)
#        print(result)
#    else:
#        result=0
#    return result
#print("\n\nRecursion Example results")
#tri_recursion(16)

    # LAMBDA
#adding 10 to argument a and return the result
x=lambda a : a+10
print(x(5))
x= lambda a, b :a*b
print(x(5,6))
x=lambda a,b,c:a+b+c
print(x(5,6,2))
#using lambda to make a func that always doubles the num i sent in
def myfunc(n):
    return lambda a: a * n
mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mytripler(11))
print(mydoubler(11))

    # ARRAYS

#axess the element by refering to the index number
cars=["Volvo","Ford","BMW"]
x=cars[0]
print(x)
#modify the value of the first array item:
cars[0]="Toyota"
print(cars)
for x in cars:  #Looping
    print(x)
cars.append("Honda")    #adding array elements
#cars.pop(1) #removing the 2 element
#cars.remove("Volvo")
# ARRAY Methods
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

    # CLASSES and OBJECTS

#creating a class with a property named x :
class MyClass:
    x=5
print(MyClass)
#Creating Object
p1=MyClass()
print(p1.x)
#create a class named Person,use the __init__() function to assign values for name and age:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Ilija", 27)
print(p1.name)
print(p1.age)
#insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
p1=Person("John",36)
p1.myfunc()
#modify object properties
p1.age=40
#del p1.age
#del p1
print(p1.age)

    # Python INHERITANCE

#Creating Parent class
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)
#using the Person class to create and object and then executing the printname method
x=Person("John","Doe")
x.printname()
#Creating Child Class
class Student(Person):#creating class Student that will inherit Person properties and methods
    pass    #using pass when we do not want to add more properties and methods
x=Student("Mike","Olsen")
x.printname()
#__init__() method
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        #Person.__init__(self,fname,lname)  #instead of super() method above
x=Student("Mike","Olsen")
x.printname()
#add property called  graduation year to the student class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
# /////
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
#add method called welcome to the Student class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

    # ITERATORS

#return an iterator from a tuple and print each value
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#strings are iterable objects
mystr="banana"
myit=iter(mystr)
print(next(myit)) #one of this for each letter
#Looping trough an Iterator
mytuple=("apple","banana","cherry")
for x in mytuple:
    print(x)
for x in mystr:
    print(x)
#Create an Iterator that returns numb. starting from 1,and each sequence will increase by one (ret.1,2,3,4,5etc.)
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter)) #1
print(next(myiter)) #2
print(next(myiter)) #3
print(next(myiter)) #4
print(next(myiter)) #5
#Stopiteration method (stop after 20 iterations)
class MyNumbers():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
for x in myiter:
    print(x)
    # SCOPE
#Local Scope
def myfunc():
    x=300
    print(x)
myfunc()
#local variable can be acessed from a func within the function:
def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()
#Global Scope
x=310
def myfunc():
    print(x)
myfunc()
print(x)
#printing first local and then global func
x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)
#if you use the global variable ,the var. belongs to the global scope
def myfunc():
    global x
    x=310
myfunc()
print(x)
#changing value of a global variable inside a function
x=400
def myfunc():
    global x
    x=390
myfunc()
print(x)

    # MODULES
#first we create file named mymodyle.py
import mymodule
mymodule.greeting("Ilija")

import mymodule
a=mymodule.person1["age"]
print(a)
#creating, renaming module alias as
import mymodule as mx
a=mx.person1["country"]
print(a)
#buit in modules
import platform
x=platform.system()
print(x)

import platform
x=dir(platform)
print(x)
#import from module only parts by using from keyword
from mymodule import person1
print(person1["age"])




