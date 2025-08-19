
import numpy as np

arr = np.random.randint(1, 100, size=20)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Original Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
