
# converting 1D array with 12 elements into a 2-d array.
import numpy as np
R = np.array([0,1,2,3,4,5,6,7,8,9])

print(R[2:5])
print(R[:4])
print(R[6:]) 
print(R[:]) 


A = np.array([ 
[11, 12, 13, 14, 15], 
[21, 22, 23, 24, 25], 
[31, 32, 33, 34, 35], 
[41, 42, 43, 44, 45], 
[51, 52, 53, 54, 55]]) 

print(A[:3, 2:]) 
print(A[3:, :]) 
print(A[:, 4:])
print(A[::2, ::3]) 
print(A[::, ::3]) 