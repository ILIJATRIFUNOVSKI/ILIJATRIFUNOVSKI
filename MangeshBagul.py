print("Python program to print 'Hello World!'")
print("Hello World!")
print("Find DataType of given values.")
a="Ilija"
b=12
c=15.5
d=True
e=23
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("Write proram to accept Student details 'from' user 'and print' the same")
"""name=input("Enter Student Name: ")
ID=int(input("Enter Student ID: "))
Edu=input("Enter Education: ")
p=float(input("Enter Percentage: "))
print()
print("Student Name is: ",name)
print("Student ID is: ",ID)
print("Student Education is:",Edu)
print("Student Percentage is: ",p)"""
print("Print Python version using python code")
import sys
print("Python Version")
print(sys.version)
print("Write the program to take the '2' value 'in float from' the user 'and' perform"
      "multiplication 'and' addiction")
"""num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

mul=num1*num2
print("Multiplication is: ",mul)

sum=num1+num2
print("Addition is:",sum)"""
print("Write pyton code to accept '2' numbers 'from' user 'and' display"
      "add,sub,mul and div")
"""x=int(input("First Number: "))
y=int(input("Second Number: "))
a=x+y
print("Addition: ",a)
b=x-y
print("Substraction: ",b)
c=x*y
print("Multiplication: ",c)
d=x/y
print("Division: ",d)"""
print("Write Python program to take the '2' value 'from' the user 'and' perform "
      "Modulus and Division(Floor) and Power")
"""a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
mod=a%b
print("Modulus: ",mod)
div=a//b
print("Division(Floor): ",div)
pow=a**b
print("Power: ",pow)"""
#SWAPPING
print("Write a program to accept 2 number and swap them without using 3rd variable.")
"""a=int(input("Enter First number: "))
b=int(input("Enter Second number: "))
a=a+b
b=a-b
a=a-b
print()
print("After swapping a is: ",a)
print("After swapping b is: ",b)"""
print("Take a number from user as an input update the value by adding 10,followed by multiplying by 6,"
      "and lastly get floor division by 6.")
num=10
print("Number: ",num)
sum=num+10
print("Update: ",sum)
mul=sum*6
print("Multiplication: ",mul)
floor=mul//6
print("Floor division: ",floor)
print("Write a Python code to find Area of Circle.")
"""r=float(input("Enter radious of circle: "))
area=((3.14)*(r*r))
print("Area of circle is: ",area)"""
print("Declare a student's score in 5 subjects,and calculate total score and percentage.")
"""sub1=int(input("Math: "))
sub2=int(input("Physics: "))
sub3=int(input("History: "))
sub4=int(input("English: "))
sub5=int(input("Chemistry"))
print()
total=sub1+sub2+sub3+sub4+sub5
print("Total Score: ",total)
percentage=(total/500)*100
print("Percentage: ",percentage)"""
print("Write a program to accept 2 number and swap them with using 3rd variable.")
"""a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
temp=a
a=b
b=temp
print("After Swapping value of a:",a)
print("After Swapping value of b:",b)"""
#Bitwise Operations
print("Declare the value as x=True and y=False and test the condition for 'and','or' 'not' and produce the result")
x=True
y=False
a=x&y
print("x and y result is:",a)
b=x|y
print("x or y result is:",b)
c=x!=y
print("x is not equal to y result is:",c)
print("Declare a=60 b=13 c=0 and perform all the bitwise operation where c will be storing the result"
      "on the interpreter showing the output")
a=60
b=13
c=0
c=a&b
print("a and b is:",c)
c=a|b
print("a or b is:",c)
c=a^b
print("a XOR b is:",c)
c=a<<2
print("a left shift is:",c)
c=a>>2
print("a right shift is:",c)
print("Declare a variable num=10, use short hand operator to increment num by 10,substract by 5,"
      "divide by 3 and multiply by 4")
num=10
num+=10
print("Increment:",num)
num-=5
print("Substract:",num)
num/=3
print("Divide:",num)
num*=4
print("Multiply",num)
print("Write a program to check wheter enter number is 'Even' or 'Odd'.")
num=8
if(num%2==0):
      print("Number is Even")
else:
      print("Number is Odd")
print("Write a program to check wheter enter number is 'Positive', 'Negative' or 'Zero'.")
#num=int(input("Enter Number:"))
num=10
if num>0:
      print("Number is Positive")
elif num<0:
      print("Number is Negative")
else:
      print("Number is 0")
print("Write a program to take three input for x,y and z.Then compare and find the largest value among the three num.")
"""x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))
if x>y and x>z:
      print(x,"is greater value")
elif y>z:
      print(y,"is greater value")
else:
      print(z,"is greater value")"""
print("Write a Program to Check enter year is leap year or not")
"""year=int(input("Enter Year:"))
y=year
if (y%4==0) and (y%100!=0) or (y%400==0):
      print(year,"is Leap Year")
else:
      print(year,"is not Leap Year")"""
print("Try to find wheter the alphabet is present in given string or not")
"""string="python is easy to learn"
char=input("Enter character to check:")
if char in string:
      print(char,"is present in",string)
else:
      print(char,"is not present in",string)"""
print("WAP to calculate area of triangle")
"""b=float(input("Enter base:"))
h=float(input("Enter height:"))
area=0.5*b*h
print("Area of height is:",area)"""
"""print("Wap to calculate volume of sphere")
r=float(input("Enter radius: "))
volume=(4/3)*3.14*(r**3)
print("Volume of sphere is:",volume)"""
print("WAP to display the grade given a mark by using following constraint -:")
"""Constraints-:
75&above-:A grade
60-74 -:B grade
35-59 -:C grade
Below 35 -: Fail"""

"""marks=int(input("Enter Marks: "))
if marks >=75:
      print("A grade")
elif marks>=60:
      print("B grade")
elif marks>=35:
      print("C grade")
elif marks<=35:
      print("Fail")"""
print("Take the three side for the triangle from the user and check whether the triangle is equilateral,"
      "isosceles or scalene triangle")
"""x=int(input("Enter first side: "))
y=int(input("Enter second side: "))
z=int(input("Enter third side: "))
if x==y==z:
      print("Equilateral Triangle")
elif x==y or y==z or z==x:
      print("Isosceles Triangle")
else:
      print("Scalene Triangle")"""
print("Write the program to check the number is palindrome or not") #num that remains the same when digits are changed
"""i=int(input("Enter number: "))
rev=0
x=i
while i>0:
      rev=(rev*10)+i%10
      i=i//10
if x==rev:
      print(x,"is palindrome number")
else:
      print(x,"is not palindrome")"""
print("WAP to print the sum of 1st nth natural numbers using while loop")     #num=3 3+2+1
"""sum=0
num=int(input("Enter a number: "))
while num>0:
      sum+=num
      num-=1
print("The result is:",sum)"""
print("WAP to calculate factorial of given input n using while loop")
"""num=int(input("Enter a number: "))
fact=1
while num>0:
      fact=fact*num
      num=num-1
print("factorial number is:",fact)"""
print("Print the table of the number using while loop")
"""table=int(input("Enter number:"))
i=1
while i<=10:
      print(i,"*",table,"=",i*table)
      i=i+1"""
print("Print 1-10 using while loop")
count=1
while count<=10:
      print(count)
      count+=1
print("WAP to print 10-1 using while loop")
count=10
while count>=1:
      print(count)
      count-=1
print("Reverse a number in Python input-:7546 output-:6457")
""""i=int(input("Input:"))
rev=0
while i>0:
      rev=(rev*10)+i%10
      i=i//10
print("Output:",rev)"""
print("Write a program to find the number is Armstrong number or not")  # 555 371
"""num=int(input("Enter number:"))
sum=0
temp=num
while temp>0:
      digit=temp%10
      sum+=digit**3
      temp//=10
if num==sum:
      print(num,"is Armstrong Number")
else:
      print(num,"is not Armstrong Number")"""
print("WAP to check wheter the given number is Neon or not")      #9 13
"""num=int(input("Enter a Number:"))
sqr=num*num
sum_of_digit=0
while sqr>0:
      sum_of_digit=sum_of_digit+sqr%10
      sqr=sqr//10
if num==sum_of_digit:
      print("Neon number \n")
else:
      print("Not a Neon number\n")"""
print("WAP to calculate the factorial of number using for loop")
"""num=int(input("Enter Number:"))
fact=1
for i in range(1,num+1):
      fact=fact*i
print("Factorial number is:",fact)"""
print("Write the program to accept the 5 value from the user and find the largest and the smallest among them")
"""n=int(input("Enter first number:"))
g=n
s=n
for i in range(4):
      n=int(input("Enter next number:"))
      if n>g:
            g=n
      if n<s:
            s=n
print()
print("Largest number is:",g)
print("Smallest number is:",s)"""
print("Print all odd numbers between 10 and 20 in reverse order using for loop")
for i in range(20,10,-1):
      if i%2==1:
            print(i)
print("print the following pattern"
      "****"
      "****"
      "****"
      "****"
      "****")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      print("*" *n)"""
print("WAP to check enter number is Prime or not")
"""num=int(input("Enter any number:"))
if num>1:
      for i in range(2,num):
            if (num%i)==0:
                  print(num,"is not prime number")
                  break #try with 15 without break
      else:
            print(num,"is prime number")"""
print("Print the following pattern"
      "A A A A A"
      "B B B B B"
      "C C C C C"
      "D D D D D"
      "E E E E E")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+1):
            print(chr(64+i),end=" ")
      print()"""
print("Print the following pattern"
      "1 1 1 1 1"
      "2 2 2 2 2"
      "3 3 3 3 3"
      "4 4 4 4 4"
      "5 5 5 5 5")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+1):
            print(i,end=" ")
      print()"""
print("Print the following pattern"
      "A B C D E"
      "A B C D E"
      "A B C D E"
      "A B C D E")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+1):
            print(chr(64+j),end=" ")
      print()"""
print("Print the following pattern")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+1):
            print(n+1-i,end=" ")
      print()"""
print("Print the following pattern:"
      "5 4 3 2 1"
      "5 4 3 2 1"
      "5 4 3 2 1"
      "5 4 3 2 1")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+1):
            print(n+1-j,end=" ")
      print()"""
print("Print the following pattern"
      "*"
      "**"
      "***"
      "****"
      "*****")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,i+1):
            print("*",end=" ")
      print()"""
print("Print the following pattern"
      "1"
      "22"
      "333"
      "4444"
      "55555")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,i+1):
            print(i,end=" ")
      print()"""
print("Print the following pattern"
      "1"
      "12"
      "123"
      "1234"
      "12345")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,i+1):
            print(j,end=" ")
      print()"""
print("A"
      "AB"
      "ABCD"
      "ABCDE")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,i+1):
            print(chr(64+j),end="")
      print()"""
print("*****"
      "****"
      "***"
      "**"
      "*")
"""n=int(input("Enter number of rows:"))     #Look at this
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print("*",end=" ")
      print()"""
print("11111"
      "2222"
      "333"
      "44"
      "5")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(i,end=" ")
      print()"""
print("12345"
      "1234"
      "123"
      "12"
      "1")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(j,end=" ")
      print()"""
print("AAAAA"
      "BBBB"
      "CCC"
      "DD"
      "E")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(chr(64+i),end=" ")
      print()"""
print("ABCDE"
      "ABCD"
      "ABC"
      "AB"
      "A")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(chr(64+j),end=" ")
      print()"""
print("54321"
      "5432"
      "543"
      "54"
      "5")
"""n=int(input("Enter number of rows:"))
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(n+1-j,end=" ")
      print()"""
print("*"
      "**"
      "***"
      "****"
      "***"
      "**"
      "*")
"""for i in range(4):
      for j in range(i):
            print("*",end=" ")
      print()
for i in range(4):
      for j in range(4-i):
            print("*",end=" ")
      print()"""
print("WAP to print fibonacci series till nth input value using while loop")
n=10
n1=0
n2=1
i=0
while i<n:
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
      i+=1
print("WAP to print fibonacci series using for loop")
n=10
n1=0
n2=1
i=0
for i in range(10):
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
print("Print right triangle start pattern "
      "     *"
      "    **"
      "   ***"
      "  ****"
      " *****")
size=5
for i in range(size):
      for j in range(1,size-i):
            print(" ",end="")       #first"" without space the * is on the other side
      for k in range(0,i+1):
            print("*",end="")
      print()
print("Right triangle start pattern"
      "   *"
      "  ***"
      " *****"
      " ******"
      "********")
n=5
for i in range(n):
      for j in range(n-i-1):
            print(" ",end="")
      for k in range(2*i+1):
            print("*",end="")
      print()
print("WAP to list out all the leap years from 1900-2030 using for loop")
list=[]
for i in range(1900,2031):
      if i%400==0:
            list.append(i)
      elif i%4==0:
            if i%100!=0:
                  list.append(i)
print(list)
print("Write a program to create the list between 20 and 50(including both)& print all the "
      "prime numbers within the specified range()")
l=[]
for i in range(20,51):
      for j in range(2,i):
            if i%j==0:
                  break
      else:
            l.append(i)
print(l)
print("Reverse the following list without using reverse method.Use for loop to iterate."
      "myList=[10,'abc',20,3.5,'xyz']")
myList=[10,"abc",20,3.5,"xyz"]
newList=[]
for i in range(1,len(myList)+1):
      newList.append(myList[-i])
print(newList)
print("Write a program to find the sum of the element in the list.")
list1=[3,4,5,9,10,24]
sum=0
for i in list1:
      sum=sum+i
print("The sum is :",sum)
print("Write the program to find the lists consist of at least one common element.")
list1=[1,2,3,4,5,6]
list2=[7,8,9,2,10]
for x in list1:
      for y in list2:
            if x==y:
                  print("Common element is:",x)
print("x=[2,4,6,8,10] write a code to add a element 'eleven' inside list at the end")
x=[2,4,6,8,10]
x.append('eleven')
print(x)
print("Perform an operation to merge the list y inside list x")
x=[2,4,6,8,10]
y=[12,13,14]
x=x+y
print(x)
print("Perform an operation to get reverse output")
x=[2,4,'six',8,'ten']
x.reverse()
print(x)
print("Perform pop operation and remove 'six' and remove element 8 using remove method")
y=[2,4,'six',8,'ten']
y.pop(2)
print(y)
y.remove(8)
print(y)
print("Write code to get the following output 'subscribe and learn more'")
x=["subscribe","and","learn","more"]
y=" ".join(x)
print(y)
print("Execute the following functions of list 1.Index 2.Count 3.Sort 4.Reverse()")
l=[5,2,7,2,8,2]
print("Index:",l.index(8))
print("Count:",l.count(2))
l.sort()
print("Sort:",l)
l.reverse()
print("Reverse:",l)
print("Python program to check even or odd number from the given list")
l=[47,2,66,45,8,4]
a=[]
b=[]
for i in l:
      if i%2==0:
            a.append(i)
      else:
            b.append(i)
print("List of Even Number:",a)
print("List of Odd Number:",b)
print("Python program to count Even and Odd numbers in a List")
list1=[10,21,4,45,66,93,1]
even_count, odd_count=0,0
for num in list1:
      if num%2==0:
            even_count+=1
      else:
            odd_count+=1
print("Even numbers in list:",even_count)
print("Odd numbers in list:",odd_count)
print("Python program Find unique item in a list")
list1=[1,2,2,5,8,4,4,8]
l1=[]
count=0
for item in list1:
      if item not in l1:
            count+=1
            l1.append(item)
print("No of Unique items are:",count)
print("Unique items\n",l1)
print("Lengthof list1 is:",len(list1))
print("display following output of the list"
      "[4,6,8]"
      "[1,3,5,7,9]"
      "[1,2,3,4,5,6,7,8,9]")
list=[1,2,3,4,5,6,7,8,9]
print(list[3:9:2])
print(list[::2])
print(list[::])
print("Wap to print Hollow Square Pattern")
n=5
for i in range(n):
      for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                  print("*",end="")
            else:
                  print(" ",end="")
      print()
print("WAp to print Square Pattern in Python")
for i in range(0,5):
      print("*" *5)
print("Hollow Square Pattern in Python")
n=5
for i in range(n):
      if i==0 or i==n-1:
            print("*" * n)
      else:
            print("*"+" "*(n-2)+"*")
print("Right triangle star pattern")
n=5
for i in range(1,n+1):
      print(" "*(n-i)+"*"*i)
print("Downward triangle star pattern")
n=5
for i in range(n):
      print("*"*(n-i))
print("Piramid pattern in Python")
n=5
for i in range(n):
      print(" "*(n-i-1)+"*"*(2*i+1))
print("Right pascal triangle pattern")
n=5
for i in range(n):
      print("*"*(i+1))
for i in range(n):
      print("*"*(n-i-1))
print("Print left triangle star pattern")
n=5
for i in range(1,n+1):
      print("*"*i)
print("Write a program to create the list between 20 to 50 "
      "& print all the prime numbers within the specified range()")
l=[]
for i in range(20,50):
      for j in range(2,i):
            if i%j==0:
                  break
      else:
            l.append(i)
print(l)
print("Reverse the following list without using reverse method.Use for loop to iterate.")
myList=[10,"abc",20,3.5,"xyz"]
newList=[]
for i in range(1,len(myList)+1):
      newList.append(myList[-i])
print(newList)
print("Using list comprehension, store cubes of natural number from 1-20 in a list")
s=[x**3 for x in range(1,21)]
print(s)
print("Given a list grammar, using list comprehension,filter all the negative words"
      "that starts with 'n'")
grammar=['is','not','am','are','do','did','no','will','never',
         'shall','none','was','nor']
lib=[i for i in grammar if 'n' in i]
print(lib)
print("Given a list lib, using list comprehension store all the books"
      "that were published after 2010")
library=[('book1',2002),('book2',2012),
         ('book3',2007),('book4',2015),
         ('book5',2005),('book6',2018)]
lib=[library[s] for s in range(len(library))
     if library[s][1]>=2010]
print(lib)
print("Using list comprehension store all the even numbers from 1 to 100 in a list")
s=[x for x in range(1,101) if x%2==0]
print(s)
#print("Used only list comprehension "
#      "Using lambda to print table of 10")
#numbers=list(map(lambda i:i*10,
#                 [i for i in range(1,6)]))
#print(numbers)
print("Use list comprehension to store a list of all numbers divisible by 3 and 5,"
      "between 1 to 30")
l1=[i for i in range(1,31) if i%3==0
                     and i%5==0]
print(l1)
print("Write a code to get the following output 'I love python program','I Love Python Program',etc")
x='i LoVe pYtHoN ProgrAm'
print(x.capitalize())
print(x.title())
print(x.lower())
print(x.upper())
print(x.split())
print("Use format method to inject the following name and variable in given variable named string")
name="python"
age=30
string="my name is {} and my age is {}."
print(string.format(name,age))
print("Write a code to retrieve the word 'pYtHoN' by using slicing from variable x ")
x='i LoVe pYtHoN PrOGrAm'
print(x[7:13])
print("Python code to Count Alphabets,Numeric values and space")
str="Subscribe 1 million"
alphabets,num,space=0,0,0
for i in range(len(str)):
      if str[i].isalpha():
            alphabets+=1
      elif str[i].isdigit():
            num+=1
      elif str[i].isspace():
            space+=1
print("Alphabet letters:",alphabets)
print("Numbers:",num)
print("Space:",space)
print("Python code to count Alphabets,Numeric,Special character using function")
str='guido_van_rossum_1989'
alphabets,num,special=0,0,0
for i in range(len(str)):
      if str[i]>='a' and str[i]<='z':
            alphabets+=1
      elif str[i]>='0' and str[i]<='9':
            num+=1
      else:
            special+=1
print("Alphabet letters:",alphabets)
print("Numbers:",num)
print("Special characters:",special)
print("Research and execute the following string functions 1)replace 2)find")
s="alex is good boy"
print(s.replace("alex","Ilija"))
print(s.find("good"))
print("Take a sentence from user and find the total number of words that has been present in that sentence")
"""s=input("Enter your string\n")      #Alex is good boy, sometime less good boy
b=s.lower()
b=b.split()
d={}
i=0
for i in b:
      if i in d:
            continue
      else:
            d[i]=b.count(i)
for i,j in d.items():
      print(i,j)"""
print("Generate a list of numbers divisible by 5.[comprehension]")
l=[x for x in range(1,100) if x%5==0]
print(l)
print("Q1:Write the code to count the frequency of 1"
      "Q2:Write a code to merge tuple t with(11,12,13,14)&and store in variable named newt")
t=(2,1,4,6,2,1,4,1,2,7,1)
print(t.count(1))

t1=(11,12,13,14)
newt=t+t1
print(newt)
print("Given a list of tuples-Every tuple consist of batsman's name and runs"
      "a)calculate the total score"
      "b)create a list of batsman who scored more than 50")
l1=[("V Kohli",100),("R Sharma",80),("R Pant",27),("P Shaw",34)]
a=0
for i in l1:
      a=a+i[1]
print("Total score is:",a)

l2=[i[0]for i in l1 if i[1]>=50]
print(l2)
print("Store 5 names as an input,find the name which have maximum alphabets in it.")
"""name=input("Enter names:")
max=len(name)
a=name
for i in range(4):
      name=input("Enter names:")
      if len(name)>max:
            max=len(name)
            a=name
print()
print(a)"""
print("Use list comprehension where possible input data='abc@#123' -expected output dict alphabets,"
      "digits, symbols")
s="abc@#123"
d={}
d["Alphabets"]=[]
d["digits"]=[]
d["Symbols"]=[]
for i in s:
      if i.isalpha():
            d["Alphabets"].append(i)
      elif i.isnumeric():
            d["digits"].append(i)
      else:
            d["Symbols"].append(i)
print(d)
print("Write a program to get a list sorted in increasing order by the last element in each tuple from a given,"
      "list of non-empty tuples.")
l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(l)):
      for j in range(len(l)):
            if l[i][1]<l[j][1]:
                  l[i],l[j]=l[j],l[i]
print(l)
print("Given two list x and y, using list comprehension take the cross product of x and y")
x=[1,2,3]
y=['a','b','c']
new=[(x[a],y[b]) for a in range(len(x))
      for b in range(len(y))]
print(new)
print("Creating a virus")
"""from turtle import *
speed(10)
color('cyan')
bgcolor('black')
b=200
while b>0:
      left(b)
      forward(b*3)
      b=b-1"""
print("Reverse string in Python using string slicing")
string='python'
rev_str=string[::-1]
print(rev_str)
print("Reverse string in Python using reversed() funcstion")
string='python'
rev=reversed(string)
rev_str="".join(rev)
print(rev_str)
print("Reverse string in Python using string recursion")
def reverse(string):
      if len(string)==0:
            return string
      else:
            return reverse(string[1:])+string[0]
string='python'
print(reverse(string))
print("Reverse string in Python using for loop")
string='python'
rev_str=""
for s in string:
      rev_str=s+rev_str
print(rev_str)
print("Reverse string in Python using whileloop")
string='python'
rev_str=""
length=len(string)-1
while length>=0:
      rev_str+=string[length]
      length-=1
print(rev_str)
print("Square of list elements using map() function in Python.")
#def square(n):
#      return n**2
#List=[1,2,3,4,5]
#squares=list(map(square, List)) #PRoblem with mapping
#print(squares)
print("WAP to find fibonacci sequence in List")
fib=[0,1]
[fib.append(fib[-2]+fib[-1])
 for i in range(8)]
print(fib)
print("Password input like hide password")
"""from getpass import getpass
username=input('Enter username: ')
password=getpass('Enter password: ')"""
print("Multiple user inputs using map() and split() function in Python")
"""values=input("Enter values:").split()
a,b,c=map(int,values)
print(a,b,c)"""
print("Print Emojis using Python.")
print("\U0001F917")
print("Password input like hide password")
print("Strings formating types")
name='python'
print("I love "+ name)
print("I love {}".format(name))
print(f"I love {name}")
print("Print the following pattern:")
n=4
count=10
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(count,end=" ")
            count=count-1
      print()
print("Draw the following pattern")
n=5
for i in range(70,65,-1):
      for j in range(n):
            print(" ",end="")
      for j in range(65,i):
            print(chr(j),end="")
      n+=1
      print()
print("Draw the following pattern:")
n=3
for i in range(0,n):
      for j in range(0,n-i-1):
            print(end=' ')
      for j in range(0,i+1):
            print("* ",end="")
      print()
for i in range(n-1,0,-1):
      for j in range(n,i,-1):
            print(end=" ")
      for j in range(0,i):
            print('* ',end="")
      print()
print("Draw the following pattern")
num=5
row=5
for row in range(1,row+1):
      for col in range(1,2*num):
            if(row==num or row+col==num+1 or col-row==num-1):
                  print("*",end="")
            else:
                  print(end=" ")
      print()
print("Draw the following pattern")
row=3
for i in range(1,row+1):
      for j in range(1,row+1-i):
            print(" ",end="")
      for j in range(1,i+1):
            print(j,end="")
      for j in range(i-1,0,-1):
            print(j,end="")
      print()
print("Print the following pattern")
count=1
width=16
for i in range(8):
      print(("*"*count).center(width))
      count+=2
print("| |".center(width))
print("WAP to acess dictionary and element Loop trough a dictionary")
#Getting keys only
mydict={"Name":"Python","rank":1}
for x,y in mydict.items():
      print(x)
#Getting value only:
for x in mydict:
      print(mydict[x])
#Getting keys and value
for x,y in mydict.items():
      print(x,y)
print("WAP to acess dictionary and element")
#Acessing dictionary
print(mydict)
#Acessing element
print(mydict["Name"])
#Acessing Element
print(mydict.get("rank"))
print("Perform following operations on given Set,"
      "add 75 element,delete 1st element from the set,create duplicate set of x")
x={10,20,30,40,50,60}
x.add(75)
print("Add 75 element: \n",x)
x.remove(10)
print("Delete 1st element: \n",x)
new_x=x.copy()
print("After duplicate: \n",new_x)
print("Remove the key 'b' from dictionary d")
d={'a':10,'b':30,'c':50}
del d['b']
print(d)
print("Merge the dictionary x inside dictionary d")
d={'a':10,'b':30}
x={'i':11,'j':12}
d |= x
print(d)
print("Write a code to display all the values from the dictionary")
d={'a':10,'b':30,'c':50,'d':100}
print(d.values())
print("Write a code to add new key,value 'e':600 respectively inside dictionary d")
d['e']=600
print(d)
print("Check if key 'e' is present in dictionary d")
if 'e' in dict.keys(d):
      print("'e' is present")
else:
      print("'e' key does not exist")
print("Write a code to update the value of key 'b' to 300")
d.update({'b':300})
print(d)
print("Write a code to merge tuple t with other & store in variable named newt")
t=(2,1,4,6,2)
t1=(11,12,13,14)
newt=t+t1
print(newt)
print("Write a code to count the Frequency of 1")
t=(2,1,4,6,2,1,4,1,2,7,1)
count=0
for i in t:
      if i==1:
            count+=1
print(count)
print("WAP to get unique numbers from the list using any loop")
numbers=[20,20,30,30,40]
def get_unique_numbers(numbers):
      unique=[]
      for number in numbers:
            if number in unique:
                  continue
            else:
                  unique.append(number)
      return unique
print(get_unique_numbers(numbers))
print("WAP to get second highest value from the list")
data=[1,2,8,3,12]
data.sort()
print("second highest value:",data[-2])
print("Print Fibonacci series 1,2,3,5,8,13 of length 10,using any loop")
length=10
n1,n2=1,2
count=0
while count<length:
      print(n1,end=" ")
      nth=n1+n2
      n1=n2
      n2=nth
      count+=1
print("Print calendar on console")
import calendar
print(calendar.month(2022, 2))
print("Write a Python function that takes a list of words and returns the length of the longest one")
"""def find_longest_word(words_list):
      word_len=[]
      for n in words_list:
            word_len.append(len(n),n)
      word_len.sort()
      return word_len[-1][0],word_len[-1][1]
result=find_longest_word(["Python","MySQL","Flask"])
print("\nLongest word: ",result[1])
print("Length of the longest word:",result[0])"""
print("Create a function to find out Cube of given number")
"""def cube(num):
      return num*num*num
num=int(input("Enter any number:"))
cb=cube(num)
print("Cube of {0} is {1}".format(num,cb))"""
print("WAP to find Minimum number from the list without using function and slicing or sorting function")
NumList=[5,44,37,3,56,83]
smallest=largest=NumList[0]
for j in range(1, len(NumList)):
      if(smallest>NumList[j]):
            smallest=NumList[j]
print("The smallest Element in this list is:",smallest)
print("Create a function calculation() such that it can accept two variables value and calculate the,"
      "addition and subtraction of them.And also it must return both addition and subtraction in a single return call")
def calculation(x,y):
      addition=x+y
      subtraction=x-y
      return addition,subtraction
c,d=calculation(20,10)
print("Addition and subtraction of number is",c,d)
print("WAP to get second highest value from the list without using sort function")
data=[1,2,8,3,12]
highest,second_highest=0,0
for a in data:
      if not highest or a>highest:
            if highest:
                  second_highest=highest
            highest=a
print("second_highest: {}".format(second_highest))
print("Count the appearance of each alphabet and store in a dictionary")
string="hello world"
dictionary={}
for i in string:
      if i in dictionary:
            continue
      elif i==" ":
            continue
      else:
            dictionary[i]=string.count(i)
print(dictionary)
print("Create a list with 10 value and find the smallest, largest and sum of all the number in the list.")
list=[11,55,22,58,87,3,23,8,104,44]
print("Smallest number is:",min(list))
print("Largest number is:",max(list))
#print("Sum of list is",sum(list))
print("WAP to count number of odd and even number from the series in the list:")
list=[2,3,4,55,56,78,75,69,66,101,100]
even_count, odd_count=0,0
for i in list:
      if i%2==0:
            even_count+=1
      else:
            odd_count+=1
print("Even numbers in the list are:",even_count)
print("Odd numbers in the list are:",odd_count)
print("WAP to count the number of strings here the str length is 2 or more and the firs and last character,"
      "are same from a given list of strings")
words=['abc','xyz','aba','1221','343','def']
count=0
for word in words:
      if len(word)>1 and word[0]==word[-1]:
            count+=1
print(count)
print("Get the list,sorted in increasing order by the last element in each tuple")
def last(n):
      return  n[-1]
def sort(tuples):
      return sorted(tuples, key=last)
a=[(1,2),(2,3),(2,1)]
print("Sorted:")
print(sort(a))
print("Join items of given list using 'and' and print the string")
weekdays=['apple','banana','grapes']
print(' and '.join(weekdays))
#print(' and '.join(str(w)) for w in weekdays))
print("Difference between del, remove(), pop()")
#del keyword
list=[11,12,13,14,15]
del list[2]
print(list)
#remove() method
list=[11,12,13,14,15]
list.remove(12)
print(list)
#pop() method
list=[11,12,13,14,15]
list.pop(2)
print(list)
print("Use filter, map ,reduce in lambda functions.")
#map function
items=[1,2,3,4,5,6]
#new_items=list(map(lambda x:x*x,items))
#print(new_items)
#filter function
items=[1,2,3,4,5,6]
#new_items=list(filter(lambda x:(x%2==0),items))
#print(new_items)
#reduce function
from functools import reduce
items=[1,2,3,4,5,6]
new_items=reduce((lambda x,y:x+y),items)
print(new_items)
print("Write a program to create function of prime number")
def operation(x):
      if x>1:
            for i in range(2,x):
                  if x%i==0:
                        print(x,"is not prime number")
                        break
            else:
                  print(x,"is prime number")
      else:
            print(x,"is not prime number")
operation(13)
print("Create a function whitch will accept temperature in Celsius and return output in Fahrenheit")
def Cel_To_Fah(n):
      return (n*1.8)+32
n=20
print("Fahrenheit is:",int(Cel_To_Fah(n)))
print("Use filter function to find only int values from a list of values given in a list")
input_list=[1,"3",'s',"hello",7,2.0]
#result=list(filter(lambda e:isinstance(e,int),input_list))
#print(result)
print("Perform following operations on given set, add 75 element, delete 1st element from the set,"
      "create duplicate set of x")
x=(10,20,30,40,50,60)
#x.add(75)
print("add 75 element:",x)
#x.remove(0)
#new_x=x.copy()
print("Print the following pattern")
n=5
for i in range(1,n+1):
      for j in range(1,n+2-i):
            print(j,end=" ")
      print()
print("3 Types of programmers")
name="Python"
print("I love "+ name)
print("I love {}".format(name))
print(f"I love {name}")

