import math

# Integer
a = 20
b = 6
print("Integer:", a)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** 2)

# Float
x = 12.75
print("\nFloat:", x)
print("Absolute:", abs(x))
print("Rounded:", round(x))
print("Ceiling:", math.ceil(x))
print("Floor:", math.floor(x))

# Complex
c = 3 + 4j
print("\nComplex:", c)
print("Real part:", c.real)
print("Imaginary part:", c.imag)
print("Magnitude:", abs(c))

# String
s = "Python Programming"
print("\nString:", s)
print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("First 6 characters:", s[:6])

# List
lst = [10, 20, 30, 40]
print("\nList:", lst)
lst.append(50)
print("After append:", lst)
print("Length:", len(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))
print("Sum:", sum(lst))

# Tuple
t = (10, 20, 30, 40)
print("\nTuple:", t)
print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))

# Dictionary
student = {
    "Name": "Sarthak",
    "Age": 18,
    "Branch": "Computer Engineering"
}
print("\nDictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Name:", student["Name"])

# Set
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("\nSet 1:", set1)
print("Set 2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

# Frozenset
fs = frozenset([10, 20, 30, 40])
print("\nFrozenset:", fs)
print("Length:", len(fs))

# Boolean
p = 10
q = 5
result = p > q
print("\nBoolean result:", result)

# NoneType
value = None
print("\nNoneType value:", value)
print("Data type:", type(value))

# Math functions
print("\nMath Functions")
print("Square root of 64:", math.sqrt(64))
print("2 raised to 5:", math.pow(2, 5))
print("Factorial of 5:", math.factorial(5))
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Cosine of 0 degrees:", math.cos(math.radians(0)))
