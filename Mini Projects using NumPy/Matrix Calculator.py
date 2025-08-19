
import numpy as np

def get_matrix(order):
    """Get matrix input from user based on order (rows, cols)."""
    rows, cols = order
    print(f"\nEnter values for a {rows}x{cols} matrix:")
    matrix = []
    for i in range(rows):
        row = input(f"  Row {i+1} (space-separated): ").strip().split()
        if len(row) != cols:
            print("❌ Invalid number of columns.")
            return None
        matrix.append([float(val) for val in row])
    return np.array(matrix)

print("🧮 Matrix Calculator - NumPy Only")
print("Select operation:")
print(" 1. Addition")
print(" 2. Multiplication")
print(" 3. Transpose\n")

choice = input("Enter choice (1/2/3): ").strip()

if choice == '1':
    rows = int(input("\nEnter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\n🔢 Matrix A")
    A = get_matrix((rows, cols))
    print("\n🔢 Matrix B")
    B = get_matrix((rows, cols))

    if A is not None and B is not None:
        print("\n✅ Result (A + B):\n", A + B)

elif choice == '2':
    rows_A = int(input("\nEnter rows for Matrix A: "))
    cols_A = int(input("Enter columns for Matrix A: "))
    print("\n🔢 Matrix A")
    A = get_matrix((rows_A, cols_A))

    rows_B = cols_A
    cols_B = int(input("Enter columns for Matrix B: "))
    print("\n🔢 Matrix B")
    B = get_matrix((rows_B, cols_B))

    if A is not None and B is not None:
        print("\n✅ Result (A x B):\n", A @ B)

elif choice == '3':
    rows = int(input("\nEnter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("\n🔢 Matrix")
    A = get_matrix((rows, cols))

    if A is not None:
        print("\n✅ Transpose:\n", A.T)

else:
    print("❌ Invalid choice.")
