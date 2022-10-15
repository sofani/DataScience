# Python Numpy and Pandas  
# Achraf Cohen - acohen@uwf.edu
# *****************************************************
# This code import NumPy library
# import numpy as np
# # Having issue importing a package use Terminal and install it:
# # python3 -m pip install --user "package.name"


# arr1 =  np.array([1,2,45,564,98]) # create array using NumPy
# print(arr1)


# # Multidimensional arrays!
# d0 = np.array(56)
# d1 = np.array([15, 52, 83, 84, 55])
# d2 = np.array([[1, 2, 3], [4, 5, 6]])
# d3 = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 21, 31], [41, 51, 61]]])

# # print dimension
# print(d0.ndim) 
# print(d1.ndim)
# print(d2.ndim)
# print(d3.ndim)

# arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]], dtype=int)

# print(arr2)

# print('4th element on 1st dim: ', arr2[0, 3])

# print('4th element on 2nd dim: ', arr2[1, 3])

# print('1st dim: ', arr2[0, :])

# arr3 = np.array([1, 2, 3, 4, 5, 6, 7])

# print("From the start to index 2 (not included): ", arr3[:2])

# print("From the index 2 (included) to the end: ", arr3[2:])

# # Arithmetic operations and Math/Stat functions:

# import numpy as np

# a = np.array([[1,2,np.nan,4,5], [6,7,8,9,10]], dtype="f")
# b = np.array([[10,20,30,40,50], [60,70,80,90,100]], dtype="i")

# np.subtract(b,a) # b-a

# np.add(b,a) # b+a

# np.divide(b,a) # b/a

# np.multiply(b,a) # b*a

# np.exp(a) # exponential function

# np.log(a) # natural logarithm function

# np.sqrt(a) # square root function

# np.full((4,2,2),5) # 3x3 constant array

# # remove nan
# a=a[~np.isnan(a)]

# a.mean() # mean 

# a.std() # standard deviation

# a.var() # variance

# a.mean(axis=1) # mean across axis 0 (rows)

# np.median(a) # median 

# np.median(a,axis=0) # median 



# # Random numbers generation:

from numpy import random

# x = random.randint(100) # a random integer from 0 to 100
# print(x)

# x = random.rand(10) # 10 random numbers float from 0 to 1
# print(x)

# x = random.randint(100,size=10) # 10 random integers from 0 to 100
# print(x)

# x = random.randint(100,size=(10,10)) # 10x10 random integers from 0 to 100
# print(x)

# x = random.choice([100,12,0,45]) # sample one value from an array
# print(x)
# # sample values from an array
# x = random.choice([100,12,0,45],size=(10)) 
# print(x)
# # Probability sampling
# x = random.choice([100, 12, 0, 45], p=[0.1, 0.3, 0.6, 0.0], size=(10)) 
# print(x)

# x = random.normal(loc=1, scale=0.5, size=(10)) # Normal distribution
# print(x)



## Pandas 
# Pandas is a Python library. It is useful for data wrangling and working with data sets

import pandas as pd


#list
a = [1,6,8]

# # this is a panda series
series = pd.Series(a)
 print(series)

# this is data frame
# mydataframe = pd.DataFrame(a) # data frame
# mydataframe

# Dictionary is used to store data values in key:value pairs.
mydict = {
  "calories": [1000, 690, 190],
  "duration": [50, 40, 20]
}
# convert to DF
print(pd.DataFrame(mydict))

# # Save data from R



# # read data from csv file
df = pd.read_csv("carasData.csv")

df.info()

 df.head()

 df.dtypes

 df.columns

# # list of lists numpy
 df.to_numpy()

# # Select speed
df["speed"]

# # slice the rows
 df[0:4]

# # insert NaN in the row 10 in speed column
df.loc[2,"speed"] = np.nan
df.head(10)
 newdf = df.dropna() # drop NA cells
 newdf.head()

 df.fillna(value=10)

# # integer slicing
df.iloc[0:10,:]

# # 
df2 = df.loc[:,["speed","dist"]]
# # stats
# # Mean
df2.mean()
# # descriptive stats
 df2.describe()

# # apply
df2.apply(np.cumsum)

# # max of speed and dist
 df2.max(axis=1)

# # read from URL
bbnames = pd.read_csv("https://pages.uwf.edu/acohen/teaching/datasets/bbnames.csv")
 bbnames.info()
 bbnames.groupby('year')
