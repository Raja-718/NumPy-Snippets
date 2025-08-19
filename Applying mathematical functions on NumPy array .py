
import numpy as np 
 
# Apply arithmetic operations on numpy arrays 
 
 
arr1 = np.arange(16).reshape(4,4) 
arr2 = np.array([1, 3, 2, 4]) 
 
add_arr = np.add(arr1,arr2) 
sub_arr=np.subtract(arr1,arr2) 
mul_arr = np.multiply(arr1, arr2) 
div_arr = np.divide(arr1, arr2) 
mod_arr = np.mod(arr1, arr2) 
mod_arr = np.remainder(arr1, arr2) 
 
 
print("Adding two arrays:\n",add_arr) 
print("Subtracting two arrays:\n",sub_arr) 
print("Multiplying the two arrays:\n",mul_arr) 
print("Dividing the two arrays:\n",div_arr) 
print("Applying mod() function:\n",mod_arr) 
print("Applying remainder() function \n:",mod_arr)