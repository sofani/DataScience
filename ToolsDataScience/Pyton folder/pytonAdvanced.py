from math import *
import random as ra
import numpy as np
import pandas as pd

library(reticulate)
py_install("pandas")

#Numpy 
#Storing data for 1, 2, and 3 dimentional arrays 

#Lists are slow but numpy are fast (They use fixed type)
#uses contingous memory
#Application Mathematics replacement and ploting
#
nump01 = np.array([1, 2, 3, 4, 4])
print(nump01)

a = np.array([[1, 2, np.nan, 4, 5. 7], [6, 7, 8, 9, 10]], dtype="f")
a
b = np.array([[2, 3, 4, 5, 6], [7, 8, 9, 10,11], [7, 8, 9, 10,11]], dtype="i")
b
nump01.ndim
b.shape
nump01.dtype
b.size
a*b
np.subtract(b, a)
np.subtract(a, b)
np.exp(a)
np.log(a)
np.sqrt(a)
np.full((4,2, 3), 5)


#Accesing and changing specifc elements , rows and columns

nump02 = np.array([[1, 2, 3, 4, 5, 6, 7], [6, 7, 8, 9, 10, 11, 12]])
nump02.size # Size
nump02.shape # 2 by 7 array
nump02.dtype #data type('int64')
nump02.ndim # 2 dimentional array

#Get a specific Element
nump02[1][-5]
#Get specific row
nump02[0, :]
nump02[:,6]

nump02[1, 0:-1: 2]
nump02[0,2] = 20

#Initializing Different Types of Arrays
np.zeros((2,3))

np.full_like(nump02, 4)
np.random.random(nump02.shape)

np.random.randint(7)

#Pandas


