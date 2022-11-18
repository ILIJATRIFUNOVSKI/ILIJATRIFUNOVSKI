print("WAp to create a function of perfect number")
def perfect(n):
    sum1=0
    for i in range(1,n):
        if(n%i==0):
            sum1=sum1+i
    if(sum1==n):
        print("The number is a perfect number!")
    else:
        print("The number is not a perfect number!")
n=6
#n=int(input("Enter any number: "))
perfect(n)
print("Explain the following methods in statistics module with an example"
      "mean,median,mode,variance")
#Mean method calculates the arithmetic mean of the numbers in a list
import statistics
print(statistics.mean([2,5,6,9]),"mean()")
#Median method returns the middle value of numberic data in a list
print(statistics.median([1,2,3,8,9]),"median()")
#Mode method returns the most common data point on the list
print(statistics.mode([2,5,3,2,8,3,9,4,2,5,6]),"mode()")
print(statistics.variance([2,5,3]),"variance()")
print("Looping List")
fruits=['orange','apple','pearl','banana']
for fruit in fruits:
    print(fruit,end=" ")
print("Looping Tuple")
items=('one','two','three')
for item in items:
    print(item,end=" ")
print("Looping String")
items='looping'
for item in items:
    print(item,end=" ")
print("Looping a range of number")
for i in range(5):
    print(i,end=" ")
print("Looping between a range of number")
for i in range(5,10):
    print(i,end=" ")
print()
for i in range(20,31):
    print(i,end=" ")
print("Looping with step")
for i in range(0,10,2):
    print(i,end=" ")
print()
for i in range(0,10,3):
    print(i,end=" ")
print()
for i in range(10,0,-2):
    print(i,end=" ")
print("For Loop with Index")
fruits=['apple','orange','pear','kiwi']
for i in range(len(fruits)):
    print(i,fruits[i])
print("Alternate way to get the index")
for i,fruit in enumerate(fruits):
    print(i,fruit)
print("Breaking a loop")
for i in range(10):
    if i == 5:
        break
    print(i,end=" ")
print()
sum=0
for i in range(10):
    sum+=i*1
    if sum>100:
        break
print("Sum =",sum)
print("Continuing a loop")
for i in range(10):
    if i==5 or i==7:
        continue
    print(i,end=" ")
print()
print("Adding evens")
numberss=[5,12,8,9,10,11,13,14,15]
sum=0
for i in numberss:
    if i%2 !=0:
        continue
    sum+=i
print("Sum:",sum)
print("Nested for loop")
size=5
for i in range(1,size+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("For Loop with else")
for i in range(3):
    print(i)
else:
    print("Loop finished")
print("For loop with else:")
for i in range(3):
    if i==2:
        break
    print(i)
else:
    print("Loop finished")
print()
#else executed with break statement
for i in range(3):
    if i==5:
        break
    print(i)
else:
    print("Loop finished")
print("WAP which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 200"
      "and3200(both included).The numbers obtained should be printed within a comma separated sequence on a single line")
l=[]
for i in range(200,3201):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))
print("WAP which can compute the factorial of a given numbers.The results should be printed in a comma-separated"
      "sequence on a single line.Suppose the following input is supplied to the program:8 Then, the output should"
      "be 40320")
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
#x=int(input())
x=5
print(fact(x))
print("With a given integer number n,WAP to generate dictionary that contains(i,i*i) such that is an integral number"
      "between 1 and n(both included)and then the program should print the dictionary.Suppose the following input is"
      "supplied to the program.Then the output should be{1:1,2:4,3:9,4:16,5:25}")
#n=int(input())
n=8
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
print("WAP which accepts a sequence of comma separated numbers from console and generate a list and a tuple which contains"
      "every number.Suppose the following input is supplied to the program:34,67,55,33,12,98.Then the output should be"
      "['34','67','55','33','12','98']('34','67','55'...)")
#values=input()
values='34,67,55,33,12,98'
l=values.split(",")
t=tuple(l)
print(l)
print(t)
print("Define a class which has at least two methods:getString:to get string from console input printString:to print"
      "the string in upper case.Also please include simple test function to test the class methods.")
"""class InputOutString(object):
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s.upper())
strObj=InputOutString()
strObj.getString()
strObj.printString()"""
print("WAP that calculates and prints the value according to the given formula:Q=square root of[2*C*float(d)/h "
      "Following are the fixed values of C=50 and H= Dis the variable whose values should be input to your program in "
      "a comma-separated sequence.")
"""import math
c=50
h=30
value=[]
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(value))"""
print("WAP which takes 2digits X,Y as input and generates 2 dimensional array.The element value in the i-th row and j-th "
      "column of the array should be i*j.Note i=0,1...X-1,j=0,1..Y-1."
      "ex. input 3,5")
"""input_str=input()
dimensions=[int(x)for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist=[[0 for col in range(colNum)]for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col
print(multilist)"""
print("WAP that accepts a comma separated sequence of words as input and prints the words in a comma-sep. sequence after"
      "sorting them alphabetically.Suppose the following input is supplied to the program:without,hello,bag,world")
"""items=[x for x in input().split(',')]
items.sort()
print(','.join(items))"""
print("WAP that accepts a sequence of whitespace separated words as input and prints the words after removing all "
      "duplicate words and sorting  them alphanumerically.ex:hello world and practice makes perfect and hello world again")
"""s=input()
words=[word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))"""
print("WAP which accepts a sequence of comma separated 4 digit binary numbers as its input and then check wheter they are"
      "divisible by 5 are to be printed in a comma separated sequence.Ex:0100,0011,1010,1001 output 1010")
"""value=[]
items=[x for x in input().split(',')]
for p in items:
    intp=int(p,2)
    if not intp%5:
        value.append(p)
print(','.join(value))"""
print("WAP which will find all such numbers between 1000 and 3000(both included) such that each digit of the numbers is even"
      "number.The numbers obtained should be printed in a comma-separated sequence on a single line.")
values=[]
for i in range(1000,3001):
    s=str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
print("WAP that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied"
      "to the program:hello world! 123 Then, the output should be letters 10, digits 3")
"""s=input()
d={"DIGITS":0,"LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS",d["LETTERS"])
print("DIGITS",d["DIGITS"])"""
print("WAP that accepts a sentence and calculate the number of upper and lower case letters.Suppose the following input is"
      "Hello world!, output should be upper 1 lower 9")
s="Hello world!"
#s=input()
d={"UPPER":0,"LOWER":0}
for c in s:
    if c.isupper():
        d["UPPER"]+=1
    elif c.islower():
        d["LOWER"]+=1
    else:
        pass
print("UPPER",d["UPPER"])
print("LOWER",d["LOWER"])
print("WAP that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.Ex input is 9"
      "and output should be 11106")
a=9    #a=input()
n1=int("%s"%a)
n2=int("%s%s"%(a,a))
n3=int("%s%s%s"%(a,a,a))
n4=int("%s%s%s%s"%(a,a,a,a))
print(n1+n2+n3+n4)
print("Use a list comprehension to square each odd number in a list.The list is input by a seq.-sep. numb."
      "input is:1,2,3,4,5,6,7,8,9 output is:1,3,5,7,9")
values='1,2,3,4,5,6,7,8,9'     #input()
numberss=[x for x in values.split(",") if int(x)%2!=0]
print(",".join(numberss))
print("WAP that computes the net amount of a bank account based a transaction log from console input.The transaction"
      "log is shown as following D 100 W 200,D means deposit while W means withdraw, input is D300 D300 W200 D100, output"
      "should be:500")
"""netAmount=0
while True:
    s=input()
    if not s:
        break
    values=s.split(" ")
    operation=values[0]
    amount=int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)"""
print("A website requires the users to input username and password to register.WAP to check the validity of password input"
      "by users.EX passwords: ABd1234@1,a F1#,2w3E*,2We3345 and output:ABd1234@1")
"""import re
value=[]
items=[x for x in input().split(",")]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))"""
print("Write a method which can calculate square value of number using the ** operator")
def square(num):
    return num**2
print(square(2))
print(square(3))
print("Write a program to print some Python built in function documents,such as abs(), int(), raw_input()")
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
def square(num):
    """Return the square value of the input number num
    The input number must be integer."""
    return num**2
print(square(5))
print(square.__doc__)
print("Define a function which can compute the sum of two numbers")
def SumFunction(number1,number2):
    return number1+number2
print(SumFunction(10,5))
print("Define a function that can convert a integer into a string and print it in console.")
def PrintValue(n):
    print(str(n))
PrintValue(6)
print("Define a function that can recieve two integral numbers in string form and compute their sum and then print it")
def printValue(n1, n2):
    print( int(n1) + int(n2))
printValue("3","2")
print("Define a function that can accept two strings as input and concatenate them and then point in console.")
def printValue(s1, s2):
    print(s1+s2)
printValue("3","4")
print("Define a function that can accept two strings as input and print the string with maximum length in console."
      "If two stringhs have the same length,then the function should print all strings line by line.")
def printValue(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
printValue("one","three")
print("Define a func. that can accept an integer number as input and print the 'It is an even number'"
      "if the number is even otherwise print 'It is an odd number'.")
def checkValue(n):
    if n%2==0:
        print("It is an even number!")
    else:
        print("It is an odd number !")
checkValue(7)
print("Define a function which can print a dictionary where the keys are numbers between 1 and 3(both included)"
      "and the values are square of keys")
def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
printDict()
print("Define a function which can print a dictionary where the keys are numbers between 1 and 20(both included)"
      "and the values are square of keys")
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)
printDict()
print("Define a function which can generate a dictionary where the keys are numbers between 1 and 20(both included)"
      "and the values are square of keys.The function should just print the value only.")
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for k,v in d.items():
        print(v,end=" ")
printDict()
print("Define a function which can generate a dictionary where the keys are numbers between 1 and 20(both included)"
      "and the values are square of keys.The function should print just keys only")
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for k in d.keys():
        print(k,end=" ")
printDict()
print("Define a function which can generate and print a list where the values are square of numbers between 1 and20")
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li)
printList()
print("Define a function which can generate a list where the values are square of numbers betw.1 and 20(both)."
      "Then the function needs to print the first 5 elements in the list")
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[:5])
printList()
print("Define a function which can generate square list betw.1and 20(both).Then the funct. needs to print the last 5 elements")
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[-5:])
printList()
print("-||-.Then the function needs to print all the values exept the first 5 elements in the list.")
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[5:])
printList()
print("Define a function which can generate  and print a tuple where the value are square of numbers between"
      "1 and 20(both included).")
def printTuple():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))
printTuple()
print("With a given tuple,WAP to print the first half values in one line and the last half values on one line.")
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
print("WAP which can filter even numbers in a list by using filter function.")
li=[1,2,3,4,5,6,7,8,9,10]
evenNumbers=list(filter(lambda x:x%2==0, li))
print(evenNumbers)
print("WAP which can map() to make a list whose elements are square of elements.")
li=[1,2,3,4,5,6,7,8,9,10]
squaredNumbers=list(map(lambda x:x**2,li))
print(squaredNumbers)
print("WAP which can filter() to make a list whose elements are even number between 1and20(both included).")
evenNumbers=list(filter(lambda x: x%2==0, range(1,21)))
print(evenNumbers)
print("WAP which can map() to make a list whose elements are square of numbers between 1 and 20(both included).")
squaredNumbers=list(map(lambda x: x**2, range(1,21)))
print(squaredNumbers)
print("Define a class named American which has a static method called printNationality.")
class American(object):
    @staticmethod
    def printNationality():
        print("America")
anAmerican=American()
anAmerican.printNationality()
American.printNationality()
print("Define a class named Circle which can be constructed by a radius.The Circle class has a method which can compute"
      "the area")
class Circle(object):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
aCircle=Circle(2)
print(aCircle.area())
print("Define a class named Rectangle which can be constructed by a length and width.The rectangle class has a method"
      "which can compute the area.")
class Rectangle(object):
    def __init__(self, l, w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
aRectangle=Rectangle(2,10)
print(aRectangle.area())
print("Define a class named Shape and its subclass Square.The Square class has an init function which takes a length as"
      "argument.Both classes have a area function which can print the area of the shape where Shape's area is 0"
      "by deafult.")
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length=l
    def area(self):
        return self.length*self.length
aSquare=Square(3)
print(aSquare.area())
print("Write a function to compute 5/0 and use try/except to catch the exceptions")
def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except ExceptionError:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
print("Assuming that we have some email addresses in the 'username@companyname.com' format,write program to print the"
      "user name of a given email address.Both usernames and company names are composed of letters only.")
import re
emailAddress='Ilija@google.com' #input()
pat2="(\w+)@((\w+\.)+(com))"
r2=re.match(pat2,emailAddress)
print(r2.group(1))
print("Assuming that we have some email addresses in the username@companyname.com format, write a program to print the"
      "company name of a given email address.Both username and company names are composed of letters only.")
import re
emailAdress='Ilija@google.com' #input()
pat2="(\w+)@(\w+)\.(com)"
r2=re.match(pat2,emailAdress)
print(r2.group(2))
print("WAP which accepts sequence of words separated by whitespace as input to print the words composed of digits only")
import re
s='2 cats and 3 dogs' #input()
print(re.findall("\d+",s))
print("WAP to compute:f(n)=f(n-1)+100 with a given input by console (n>0).")
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100
n=6 #int(input())
print(f(n))
print("The fibonacci Sequence is computed based on the following formula:"
      "f(n) if n=0 if n=1 f(n)=f(n-1)+f(n-2) if n>1")
def f(n):
    if n==0: return 0
    elif n==1: return 1
    else: return f(n-1)+f(n-2)
n=7 #int(input())
print(f(n))
print("The fibonacci sequence is computed based on the following formula")
def f(n):
    if n==0: return 0
    elif n==1: return 1
    else: return f(n-1)+f(n-2)
n=7    #n=int(input())
values=[str(f(x))for x in range(0,n+1)]
print(",".join(values))
print("WAP using generator to print the even numbers between 0 and n in comma separated form while n is input by console")
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=7 #n=int(input())
values=[]
for i in EvenGenerator(n):
    values.append(str(i))
print(",".join(values))
print("WAP using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated"
      "form while n is input by console")
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
n=100   #n=int(input())
values=[]
for i in NumGenerator(n):
    values.append(str(i))
print(",".join(values))
print("WAP which accepts basic mathematic expression from console and print the evaluation result.")
expression="35+3" #input()
print(eval(expression))
print("Generate a random float where the value is between 10 and 100 using Python math module")
import random
print(random.random()*100)
print("Generate random float where the value is between 5 and 95 using math module.")
import random
print(random.random()*100-5)
print("WAP to output a random even number between 0 and 10 inclusive using random  module and list comprehension")
import random
print(random.choice([i for i in range(11) if i%2==0]))
print("WAP to output a random number,which is divisible bu 5 and 7,between 0 and 200 inclusive using random module and"
      "list comprehension")
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
print("WAP to generate a list with 5 random numbers between 100 and 200 inclusive")
random
print(random.sample(range(100,201),5))
print("WAP to randomly generate a list with 5 even numbers between 100 and 200 inclusive.")
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))
print("WAP to randomly generate a list with 5 numbers,which are divisible by 5 and 7 between 1 and 1000 inclusive")
import random
print(random.sample([i for i in range(1,1001) if i%2==0 and i%7==0],5))
print("WAP to randomly print a integer number between 7 and 15 inclusive.")
import random
print(random.randrange(7,16))
print("WAP to comress and decompress the string")
import zlib
s=b'hello world!hello world!hello world!hello world'
t=zlib.compress(s)
print(t)
print(zlib.decompress(t))
print("WAP to get compress the bytes of string by using zlib.compress(s) method.")
import zlib
s=b'Hello world'
print(len(s))
t=zlib.compress(s)
print(len(t))
print("WAP to print running time of execution of '1+1' for 100 times.")
"""from timeit import Timer
t=Timer("for i in range(100):1+1")
print(t.timeit())"""
print("WAP to shuffle and print the list [3,6,7,8]")
from random import shuffle
li=[3,6,7,8]
shuffle(li)
print(li)
print("WAP to generate all sentences where subject is in['I','You'] and verb is in['Play','Love'] and "
      "the object is in ['Hockey','Football']")
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey", "Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i],verbs[j],objects[k])
print(sentence)
print("WAP to print the list after removing delete even numbers in given list.")
li=[5,6,77,45,22,12,24]
li=[x for x in li if x%2!=0]
print(li)
print("By using list comprehension write a program to print the list after removing delete numbers which are divisible "
      "by 5 and 7 in list.")
li=[12,24,35,70,88,120,155]
li=[x for x in li if x%5!=0 and x%7!=0]
print(li)
print("With list comprehension WAP to print the list after removing the 0th,2nd,4th,6th number in given list.")
li=[12,24,35,70,88,120,155]
li=[x for (i,x)in enumerate(li) if i%2!=0]
print(li)
print("Use list comprehension to delete a bunch of elements from a list.Use enumerate to get(index,value) tuple.")
li=[12,24,35,70,88,120,155]
li=[x for (i,x) in enumerate(li) if i%2!=0]
print(li)
print("By using list comprehension,write a program to generate 3D array whose each element is 0.")
aRray=[[[0 for col in range(2)]for col in range(2)]for row in range(2)]
print(aRray)
print("By using list comprehension WAP to print the list after removing the 0,4,5th numbers in the given list.")
li=[12,24,35,70,88,120,155]
li=[x for (i,x) in enumerate(li) if i not in(0,4,5)]
print(li)
print("By using list comprehension WAP to print the list after removing the value 24 in given list.")
li=[12,24,35,70,88,120,155]
li=[x for x in li if x!=24]
print(li)
print("With two given lists,WAP to make a list whose elements are intersection of the above given lists.")
set1=([1,3,6,78,35,55])
set2=([12,24,35,88,120,155])
li=list(set1)
li2=list(set2)
a=[x for x in li if x in li2]
print(a)
print("With a given list,WAP to print the list after removing all duplicate values with original order reserved.")
def removeDuplicate(li):
    newli=[]
    seen=set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    return newli
li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
print("Define a class Person and its two child classes:Male and Female.All classes have a method 'getGender' which can"
      "print 'Male' for Male class and 'Female' for Female class.")
class Person(object):
    def getGender(self):
        return 'Unknown'
class Male(Person):
    def getGender(self):
        return 'Male'
class Female(Person):
    def getGender(self):
        return 'Female'
aMale=Male()
aFemale=Female()
print(aMale.getGender())
print(aFemale.getGender())
print("WAP who can count and print the numbers of each character in a string input by console.")
dic={}
s='abcdefgabc'  #input()
for s in s:
    dic[s]=dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k,v) for k,v in dic.items()]))
print("WAP which accepts a string from console and print it in reverse order.")
s='rise to vote sir'  #input()
s=s[::-1]
print(s)
print("WAP which accepts a string from console and print the characters that have even indexes(every second).")
s='H1e2l3l405w6'  #input()
s=s[::2]
print(s)
print("WAP which prints all permutations of [1,2,3].")
import itertools
print(list(itertools.permutations([1,2,3])))
print("WAP to solve a classic ancient Chinese puzzle:We count 35 heads and 94 legs among the chickens and rabbits in a"
      "farm.How many rabbits and how many chickens do we have?")
def solve(numheads,numlegs):
    ns="No solution"
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns
numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)




