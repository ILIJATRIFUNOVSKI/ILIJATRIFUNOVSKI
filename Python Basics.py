print("Write a program to print the following string in a specific format.")
print("Twinkle, twinkle, little star, \n\t\tHow i wonder what you are, \n\tUp above the world so high,\n\tLike a dimanod"
      "in the sky. \nTwinkle twinkle little star,\n\tHow I wonder what you are!")
print("WAP to display current date and time")
import datetime
now=datetime.datetime.now()
print("Current date and time")
print(now.strftime("%Y-%m-%d-%H:%M:%S"))
print("Radius of a circle from the user and compute the area")
from math import pi
r=1.1    #float(input("Imput the radius of the circle:"))
print("The area of the circle with the radius"+str(r)+" is:"+str(pi*r**2))
print("Print first and last name in reverse order with a space between them")
fname="Ilija"      #input("Input your first name:")
lname="Trifunovski"      #input("Input your last name:")
print("Hello "+lname+" "+fname)
print("Generate a list and a tuple with comma-separated numbers")
values='12,13,14,15'     #input("Input some comma separated numbers:")
list=values.split(",")
tuple=tuple(list)
print("List:",list)
print("Tuple",tuple)
print("WAP ")
print("WAP to accept a filename from the user and print the extension of that.")
filename='abc.py'   #input("Input the filename:")
f_extns=filename.split(".")
print("The extension of the file is: "+repr(f_extns[-1]))
print("WAP to display the first and last colors from the following list.")
color_list=["Red","Green","White","Black"]
print("%s %s"%(color_list[0],color_list[-1]))
print(color_list[0],color_list[-1])
print("WAP to display the examination schedule.Extract the date from exam_st_date.")
exam_st_date=(17,3,2022)
print("The examination will start from:%i / %i / %i" % exam_st_date)
print("WAP that accepts an integer(n) and computes the value of n+nn+nnn")
a='5'    #int(input("Input an integer: "))
n1=int("%s"%(a))
n2=int("%s%s"%(a,a))
n3=int("%s%s%s"%(a,a,a))
print(n1+n2+n3)
print("WAP to print the documents(syntax,description etc.)of Python built-in function(s).Sample:abs()")
print(abs.__doc__)
print("WAP to calculate number of days between two dates.Sample:(2022,3,1)(2022,3,17)")
from datetime import date
f_date=date(2022,3,1)
l_date=date(2022,3,17)
delta=l_date-f_date
print(delta.days)
print("WAP to get the volume of sphere with radius 6.")
pi=3.14
r=6
v=4.0/3.0*pi*r**3
print("The volume of the sphere is: ",v)
print("WAP to get the difference between a given number and 17,if the number is greater than 17 return double the"
      "absolute difference.")
def difference(n):
      if n<=17:
            return 17-n
      else:
            return(n-17)*2
print(difference(22))
print(difference(14))

