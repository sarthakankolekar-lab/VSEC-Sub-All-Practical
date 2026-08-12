import numpy as np

# =====================================================================
# 1. 1D Array Creation
# =====================================================================

# Direct array definition
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

# Array with start, stop, and step step-size
arr2 = np.arange(0, 10, 2)
print("\nArray using np.arange():")
print(arr2)

# Array with start, stop, and total number of elements
arr3 = np.linspace(0, 1, 5)
print("\nArray using np.linspace():")
print(arr3)


# =====================================================================
# 2. 1D Array Indexing & Slicing
# =====================================================================

print("\nIndexing:")
print("First element:", arr1[0])
print("Third element:", arr1[2])

print("\nSlicing:")
print("Elements from index 1 to 3:", arr1[1:4])
print("Reversed array:", arr1[::-1])


# =====================================================================
# 3. 2D Arrays (Matrices)
# =====================================================================

# Creating a 2D matrix
matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])
print("\n2D Array:")
print(matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)


# =====================================================================
# 4. 2D Indexing & Slicing
# =====================================================================

print("\n2D Indexing:")
print("Element at row 0, column 2:", matrix[0, 2])
print("Element at row 1, column 1:", matrix[1, 1])

print("\n2D Slicing:")
print("First row:", matrix[0, :])
print("Second column:", matrix[:, 1])


# =====================================================================
# 5. Reshaping Arrays
# =====================================================================

arr4 = np.arange(1, 7)
print("\nOriginal Array:")
print(arr4)

# Changing array structure without changing data
reshaped = np.reshape(arr4, (2, 3))
print("Reshaped 2D Array:")
print(reshaped)


# =====================================================================
# 6. Mathematical Operations
# =====================================================================

scores = np.array([78, 85, 92, 66, 74])

# Matrix-wide aggregations
print("\nMathematical Operations:")
print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))

# Scalar arithmetic applied to every single element
print("\nElement-wise Operations:")
print("Array + 10:", scores + 10)
print("Array * 2:", scores * 2)
