#NUMPY
#   Numpy is a general purpose array processing package . It provides a high performance multidimensional 
#   array object and tools for working with this arrays. It is the fundamental package for scientific 
#   computing with Python 

#Array
#   An array is a data structure that store values of same data type. In,Python this is the main difference
#   between array and lists. While python list can contain value corresponding to different data types,
#   arrays in Python can only contain values corresponding to same data type 

#Import the library

import numpy as np

lst=[1,2,3,4]
arr=np.array(lst)

print(type(arr))
print(arr.shape)

#
lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[3,4,5,6,7]

arr1=np.array([lst1,lst2,lst3])
print(arr1)
print(arr1.shape)

#Indexing
print(arr1[2])
print(arr1[1:2])

print(arr1[-1])
print(arr1[::-3])

print(arr1[0::1,4:0])



print(arr1[1:,1:3])
print(arr1[1:,3:])
print(arr1[:,3:])
print(arr1[:2 ,4:4])

#EDA

print(arr[arr<2])
print(arr1.reshape(5,3))

#Mechanism  to create array
print(np.arange(1,20,2).reshape(2,5))

print(arr1 * arr1 )

print(np.ones(5))
print(np.zeros(5))

print(np.radians(5))

print(np.random.random_sample(4))