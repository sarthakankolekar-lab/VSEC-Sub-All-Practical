import pandas as pd

# ==============================================================================
# 1. DATA STRUCTURE CREATION (SERIES & DATAFRAME)
# ==============================================================================
# Create a simple Pandas Series
marks = pd.Series([85, 90, 78, 92, 88])
print("Pandas Series:")
print(marks)

# Create a multi-column DataFrame from a dictionary
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Sarthak"],
    "Age": [18, 19, 18, 19, 18],
    "Marks": [85, 78, 92, 88, 95]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# ==============================================================================
# 2. DATA INSPECTION & EXPLORATION
# ==============================================================================
# Display the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Display descriptive statistical summary
print("\nStatistical Summary:")
print(df.describe())

# ==============================================================================
# 3. METADATA & BASIC PROPERTIES
# ==============================================================================
# Get dimensions, columns, and variable types
print("\nShape of DataFrame:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# ==============================================================================
# 4. FILE EXPORT & IMPORT (I/O OPERATIONS)
# ==============================================================================
# Save the DataFrame to a CSV file without row index numbers
df.to_csv("students.csv", index=False)
print("\nData exported successfully to students.csv")

# Read the data back from the generated CSV file
df_csv = pd.read_csv("students.csv")
print("\nData imported from CSV:")
print(df_csv)

# ==============================================================================
# 5. IMPORTED DATA VERIFICATION
# ==============================================================================
# Double-check specific slices and summary statistics of the file data
print("\nFirst 3 records:")
print(df_csv.head(3))

print("\nLast 2 records:")
print(df_csv.tail(2))

print("\nStatistical Summary:")
print(df_csv.describe())
