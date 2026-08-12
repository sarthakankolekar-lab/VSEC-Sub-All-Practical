import numpy as np

# ==========================================
# 1. CREATING ARRAYS
# ==========================================
arr1 = np.array([1, 4, 9, 16, 25]) 
arr2 = np.array([10, 20, 30, 40, 50]) 

print("Array 1:\n", arr1) 
print("\nArray 2:\n", arr2) 

# ==========================================
# 2. VECTORIZED OPERATIONS & UFUNCS
# ==========================================
# Vectorized addition using np.add()
addition = np.add(arr1, arr2) 
print("\nVectorized Addition:\n", addition) 

# Vectorized multiplication 
multiplication = arr1 * arr2 
print("\nVectorized Multiplication:\n", multiplication) 

# Universal function: square root 
square_root = np.sqrt(arr1) 
print("\nSquare Root:\n", square_root) 

# Universal function: exponential 
exp_values = np.exp(np.array([0, 1, 2, 3])) 
print("\nExponential Values:\n", exp_values) 

# ==========================================
# 3. BROADCASTING
# ==========================================
# Broadcasting with a scalar 
print("\n--- Broadcasting with a Scalar ---")
print("Original Array:", arr2) 
print("Array + 5:", arr2 + 5) 
print("Array * 2:", arr2 * 2) 

# Broadcasting with a 2D array 
matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6]
]) 
row = np.array([10, 20, 30]) 

print("\n2D Array:\n", matrix) 
print("\nArray used for Broadcasting:\n", row) 

broadcast_result = matrix + row 
print("\nBroadcasting Result:\n", broadcast_result) 

# ==========================================
# 4. MORE VECTORIZED MATHEMATICAL OPERATIONS
# ==========================================
print("\n--- Vectorized Mathematical Operations ---")
print("Array - 5:", arr2 - 5) 
print("Array / 10:", arr2 / 10)
