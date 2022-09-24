# Python Basics script 
# Dr. Cohen - acohen@uwf.edu
# This is a gentle introduction to Python basics programming
# *****************************************************
# https://support.rstudio.com/hc/en-us/articles/360023654474-Installing-and-Configuring-Python-with-RStudio
# ********************
# This is Python Code
print("Hello World!")
# Python Basics
4 + 5
x = 8
X = 9
45 > 7 
45 == 7 
"Hello " + "World"
print(str(x) + " is my number!")
x, y = "Hey", 45 # Assign values to multiple variables

# Data Type
x = str(3)    # x will be '3'
x = int(3)    # x will be 3
x = float(3)  # x is a float - 3.0
x = 1j       # x is complex
x = range(5,45)    # x is a range type
x = [1,2,1,24,54,45,2,1]  # x is a list
x = (1,2,1,24,54,45,2,1)  # x is a tuple
x = {"name" : "Ach", "age" : 85}  # x is a dict (mapping)

# Math Operations
3 + 4
5 + 2.3 
65 - 65
8/2
6**2
pow(6,2)
abs(-9)
max(5,6,45)
print("Hey"*3) # String operations

# does not work - needs extra package
cos(9)

# More math
import math as mt
mt.cos(556)
#or
from math import *
cos(56)

import random # generate random numbers
print(random.randrange(1, 10))

# Interactive commands
name_enter=input("Enter your name: ")
print("Welcome to Introduction to Pyhton, " + name_enter + "!")

n1 = input("Enter a number: ")
n2 = input("Enter a number: ")
print(n1+n2) # does not work because Python results in strings from the input 

print(int(n1)+int(n2))

# Lists
# a structure of data to store data

names = ["Kyle","Karen","James", 11, 56]
print(names)

# Index starts from 0
names[0]
names[3]
names[6]
# back of the list
names[-1]
names[0:2]

# modify values
names[1] = "Cook"
print(names)


# Function with lists
numbers = [4,5,9,6,4,12]
print(names)
print(numbers)

# Extend the list
names.extend([10])
names.extend(numbers)
print(names)

# add a new element at the end of the list
names.append(numbers)
print(names)

# Insert with an index
names.insert(2,"Hello")
print(names)

# Remove an element
names.remove("Hello")
print(names)

names.remove(numbers)
print(names)

# Pick an element
names.pop()

# Find index
names.index("James")
print(names)


# Count frequency
names.append("James")
names.count("James")
print(names)


# Sort index
names.reverse()
numbers.reverse()
nmb = numbers.copy() 
print(names)
print(nmb)


# Tuples
# A tuple CANNOT be changed
coordinates = (20,89,23)
coordinates[0]
coordinates[1] = 45 # does not work

# list of tuples
coordinates2 = [(20,89),(4,9)]
coordinates2[0]
coordinates2[1][0]
coordinates2[1] = 45 # works
coordinates2
coordinates2[0][1] = 5



# Functions
def myf(name): 
  print("Hello " + name)


myf("Jim")
myf("Achraf")
  

def mystat(x):
  stat=[x**2, mt.cos(x)]
  return(stat)

mystat(56)

# if-else statement
h = 200
if h > 2:
 print("Yes!") # indentation very important other ERROR
elif h > 50:
 print("Yes Yes!")
else:
  print("No")

# For loop
for k in range(1,11): 
  print(str(k)) # does not show up 10; goes up to 9
  
for k in numbers:
  k**2
