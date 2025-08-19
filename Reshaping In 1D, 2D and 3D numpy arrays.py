
# cconverting 1d array into 2d array
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr.reshape(4,3)
print(new_arr)

# 1D to 3D
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr2 = arr2.reshape(2,3,2)
print(new_arr2)

#Converting to 2D 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
newarr = arr.reshape(3, 3) 
print(newarr) 
 
#Converting to layers, rows and columns 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) 
newarr = arr.reshape(2, 2, 2) 
print(newarr) 
 
#Flatening the array, Converting multidimensional array to 1D array 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
newarr = arr.reshape(-1) 
print(newarr)
