import numpy as np

# Step 1: Take inputs from user until 'ok' is entered
numbers = []

print("🔢 Enter numbers one by one. Type 'ok' when done.")

while True:
    user_input = input("Enter number (or 'ok' to finish): ").strip()
    if user_input.lower() == 'ok':
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
    else:
        print("⚠️ Invalid input. Please enter a number or 'ok'.")

# Convert list to NumPy array
arr = np.array(numbers)
n = len(arr)

if n == 0:
    print("❌ No data entered.")
    exit()

# Step 2: Ask which operation to perform
print("\nChoose a calculation to perform:")
print("1. Mean")
print("2. Median")
print("3. Mode")
choice = input("Enter your choice (1/2/3): ").strip()

# Step 3: Calculate based on choice
if choice == '1':
    total = np.sum(arr)
    mean = total / n
    print("\n✅ Mean =", mean)

elif choice == '2':
    sorted_arr = np.sort(arr)
    if n % 2 == 0:
        median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        median = sorted_arr[n//2]
    print("\n✅ Median =", median)

elif choice == '3':
    unique, counts = np.unique(arr, return_counts=True)
    max_count = np.max(counts)
    mode = unique[counts == max_count]
    print("\n✅ Mode =", mode)
else:
    print("❌ Invalid choice.")
