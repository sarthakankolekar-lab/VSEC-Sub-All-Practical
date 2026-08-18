import pandas as pd

# ==============================================================================
# 1. INITIAL DATAFRAME CREATION WITH MISSING VALUES
# ==============================================================================
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Sarthak", "Neha"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE", "IT"],
    "Age": [18, 19, None, 20, 18, 19],
    "Marks": [85, None, 92, 78, 95, None],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ==============================================================================
# 2. MISSING DATA IDENTIFICATION & HANDLING
# ==============================================================================
# Detect null values across columns
print("\nMissing Values Mask:")
print(df.isnull())

print("\nTotal Missing Values per Column:")
print(df.isnull().sum())

# Impute missing numeric values using column mean
df_fill = df.copy()
df_fill["Age"] = df_fill["Age"].fillna(df_fill["Age"].mean())
df_fill["Marks"] = df_fill["Marks"].fillna(df_fill["Marks"].mean())
print("\nDataFrame After Mean Imputation:")
print(df_fill)

# Drop rows containing any missing values
df_drop = df.dropna()
print("\nDataFrame After Dropping Missing Values:")
print(df_drop)

# ==============================================================================
# 3. DATA TRANSFORMATION & CLEANING
# ==============================================================================
# Replace specific string values in categorical column
df_replace = df_fill.copy()
df_replace["Department"] = df_replace["Department"].replace("CSE", "Computer")
print("\nAfter Replacing 'CSE' with 'Computer':")
print(df_replace)

# ==============================================================================
# 4. FILTERING & SORTING
# ==============================================================================
# Filter records based on condition
print("\nStudents with Marks Greater Than 80:")
print(df_fill[df_fill["Marks"] > 80])

# Sort values in ascending and descending order
print("\nSorted by Marks (Ascending):")
print(df_fill.sort_values("Marks"))

print("\nSorted by Marks (Descending):")
print(df_fill.sort_values("Marks", ascending=False))

# ==============================================================================
# 5. GROUPING & AGGREGATIONS
# ==============================================================================
# Calculate mean marks by group
print("\nAverage Marks by Department:")
print(df_fill.groupby("Department")["Marks"].mean())

# Multi-metric group aggregation
print("\nDepartment-wise Detailed Statistics:")
print(df_fill.groupby("Department")["Marks"].agg(["count", "mean", "max", "min"]))

print("\nFinal Cleaned DataFrame:")
print(df_fill)