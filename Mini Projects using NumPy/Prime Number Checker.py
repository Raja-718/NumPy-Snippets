
import numpy as np

arr = np.random.randint(1, 100, size=20)

def is_prime_vectorized(n):
    if n < 2:
        return False
    return not np.any(np.arange(2, int(np.sqrt(n)) + 1)[:, None] @ np.ones((1, 1), dtype=bool) * (n % np.arange(2, int(np.sqrt(n)) + 1) == 0))

prime_flags = np.array([is_prime_vectorized(i) for i in arr])
primes = arr[prime_flags]
non_primes = arr[~prime_flags]

print("Array:", arr)
print("Primes:", primes)
print("Non-Primes:", non_primes)
