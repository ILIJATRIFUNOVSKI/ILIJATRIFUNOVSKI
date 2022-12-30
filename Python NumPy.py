import random

import numpy as np

#Basics
a=np.array([1,2,3], dtype='int16') #1 dimentional array
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]]) #2D float array

print(a.ndim)   #get dimension of array
print(b.shape)  #get shape
print(a.dtype)  #get type(data type)
print(a.itemsize)   #2 bites if it was int32 it would be 4 bytes
print(a.size)   #total size 3 items (a.size * a.itemsize)
print(a.size * a.itemsize)  #6 bytes (floats are bigger size than int)
print(a.nbytes) #like the upper 6 bytes

# Accessing/Changing specific elements, rows, columns, etc

a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])

print(a[1, 5])  # getting specific element [r, c]
print(a[1,-2])  #13 also
print(a[0, :])  # get a specific row
print(a[:, 2])  # get a specific column 3,10
print(a[0, 1:6:2])  # startindex : endindex : stepsize
print(a[0, 1:-1:2]) # 2,4,6
a[1, 5] = 20    # changing element
print(a)    #13 is changed to 20
a[:, 2] = 5 # every second is 5 in the 2rows
print(a)
a[:, 2] = [1,2]
print(a)    # 1row 2nd is 1 2nd row 2nd is 2

b = np.array([[[1, 2],[3, 4]],[[5, 6],[7, 8]]])   #3D array example
print(b)
print(b[0, 1, 1])   #get specific element (work inside in)  4
print(b[:, 1, :])   # 3 4  7 8
b[:, 1, :] = [[9, 9],[8,8]] #replacing
print(b)

# Initializing Different Types of Arrays

print(np.zeros((2, 3, 3)))  # all 0's matrix
print(np.ones((4, 2, 2), dtype='int32'))  # all 1's matrix with specified datatype
print((np.full((2, 2), 99, dtype='float32')))    # any other number (first one shape) 2nd the number
a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])
print(np.full_like(a, 4))   # the upper array only with all 4's (any other number)
print(np.full(a.shape, 4))  #another way
#intiliazing random
print(np.random.rand(4, 2)) #making random decimal numbers betw 0 and 1
print(np.random.random((4,2)))
print(np.random.randint(5, size=(2, 4)))    #random integer values
print(np.random.randint(-4,7, size=(2, 4)))  #random int with -4 to 7
print(np.identity(5))   # The identity matrix (only one parameter identity is square matrix)
arr =np.array([[1, 2, 3]])
r1 = np.repeat(arr,3, axis=0)   #repeating array (1 2 3 3times, axis=1 all in one row)
print(r1)
""" 11111
    10001
    10901
    10001
    11111"""
output = np.ones((5, 5))
print(output)
z = np.zeros((3, 3))
z [1, 1] = 9
print(z)
output[1:4,1:4] = z #getting the z values in output [1:-1,1:-1]
print(output)

a = np.array([1, 2, 3])
#   b=a This is not good way to copy arrays
b = a.copy()
b[0] = 100
print(a)
print(b)    #with .copy() method they are not the same

# MATHEMATICS

a = np.array([1,2,3,4])
print(a+2)  #3 4 5 6  a-2,a*2,a/2
a+=3    #3+ everything in array 4567
print(a)
b = np.array([1, 0, 1, 0])
print(a + b)    #sum of 2 arrays
#print(a**2)
print(np.sin(a))
 # Linear Algebra

a= np.ones((2, 3))
b= np.full((3, 2), 2)   #you need 3col for 3 rows for mul.
print(a)
print(b)
print(np.matmul(a, b))  #multiplying the matrices

c =  np.identity(3) #find the determinant
print(np.linalg.det(c)) #1.0
# Determinant,Trace,Singular Vector Decomposition,Eigenvalues,Matrix Norm,Inverse etc...
#check on this link https://github.com/KeithGalli/NumPy

# Statistics

stats = np.array([[1, 2, 3],[4, 5, 6]])
print(np.min(stats))    #find min 1
print(np.min(stats, axis=1))  #from each 1 4
print(np.min(stats, axis=0))    #all the val on the top because they are the mins 123
print(np.max(stats))    #6
print(np.sum(stats))    #sum of all 21
print(np.sum(stats, axis=0))    #1+4 2+5 3+6 579

# Reorganizing Arrays

before = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
#print(before.shape) #2x4
after = before.reshape((8, 1))    #reshaping the matrix ex.(4,2),(2,2,2)
print(after)
#Vertically Stacking Vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack([v1, v2])) #in one matrix v for vertivally
print(np.vstack([v1, v2, v2, v2]))   # we can make 3 copyies
#Horizontal Stack
h1 = np.ones((2, 4))
h2 = np.zeros((2,2))
print(np.hstack((h1, h2)))  #adding horizontally you can do [] or ()

# Miscellaneous
#https://github.com/KeithGalli/NumPy source of data file
print("Load data from file")
filedata = np.genfromtxt(r'C:\Users\user\Desktop\Dataa.txt',delimiter=",") #you must write whole path to read file and r
print(filedata)
#filedata.astype('int32') #copyies data into int 32 format
filedata = filedata.astype('int32') # proper way to make int format
print(filedata)
#Boolean Masking and Advanced Indexing
print(filedata > 50) #False or True everywhere
print(filedata[filedata > 50])  # you can index where is greater than 50 only those values are printed
print('exercise if any value in the colymn is >50')
print(np.any(filedata > 50, axis=0))    #if some of the val in colymn is true shows true
print(np.all(filedata > 50, axis=0))#less true only this column 196 766 999
print()
print(np.any(filedata > 50, axis=1))    #axis=1 for rows at least 1 is >50
print(np.all(filedata > 50, axis=1))    # all in the row must be >50
print("All files >50 and <100")
print(np.any(filedata>50, axis=0) & np.any(filedata<100, axis=0))   # we can use and& or or|
print(~np.any(filedata>50, axis=0) & np.any(filedata<100, axis=0))  # this is not ~ it reverses
#You can index with a list in NumPy
a= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) #get 239
print(a[[1, 2, 8]])
""" 01 02 03 04 05
    06 07 08 09 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
    26 27 28 29 30"""
# index 11 12 16 17 together
#a[2:4, 0:2] first rows then columns
# How would you index 2 8 14 20
#a[ [0,1,2,3],[1,2,3,4] ] first rows then columns
#How would you index 4 5   24 25 29 30
#a[[0,4,5],3:] you can do 3,4 or 3:5