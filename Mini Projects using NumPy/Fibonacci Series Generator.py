
import numpy as np

n = int(input("Enter how many Fibonacci numbers to generate: "))

fib = np.zeros(n, dtype=int)
if n > 0:
    fib[0] = 0
if n > 1:
    fib[1] = 1
for i in range(2, n):
    fib[i] = fib[i - 1] + fib[i - 2]

print("Fibonacci Series:", fib)
