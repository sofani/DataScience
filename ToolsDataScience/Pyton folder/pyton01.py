from math import *
import random as ra
print (ra.randrange(1, 10))

firstNum = input("Enter 1st Number : ")
secNum = input("Enter 2st Number : ")

result = float(firstNum) + float(secNum)
result
print("Hello World!")

x = "HeyHey"
y = 40
x
#> 'HeyHey'
y
#> 40
x, y = "Hey", 45 # Assign values to multiple variables
print(x)
#> Hey
print(y)
#> 45
ranks = ["first","second","third"] # list
x, y, z = ranks
print(ranks)
#> ['first', 'second', 'third']
x
#> 'first'
y
#> 'second'
z
#> 'third'
def myf():
  x="Hello"
  print(x)
  
myf()
#> Hello
def myf():
  global x # x to be global - outside the function
  x="Hello"
  print(x)
  
myf()
#> Hello
x = str(3)    # x will be '3'
x = int(3)    # x will be 3
x = float(3)  # x is a float - 3.0
x = 1j       # x is complex
x = range(5,45)    # x is a range type
x = [1,2,1,24,54,45,2,1]  # x is a list
x = (1,2,1,24,54,45,2,1)  # x is a tuple
x = {"name" : "Ach", "age" : 85}  # x is a dict (mapping)
