
import numpy as np

length = int(input("Enter password length: "))

# Define character set (upper + lower + digits + special)
chars = np.array(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!"))
password = ''.join(np.random.choice(chars, size=length))

print("🔐 Generated Password:", password)
