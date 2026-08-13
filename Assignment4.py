import numpy as np

# ==============================================================================
# 1. RANDOM NUMBER GENERATION
# ==============================================================================
# Uniform distribution between 0 and 1
random_uniform = np.random.rand(5)
print("Random numbers using np.random.rand():")
print(random_uniform)

# Standard normal distribution (mean=0, std=1)
random_normal = np.random.randn(5)
print("\nRandom numbers using np.random.randn():")
print(random_normal)

# Random integers between a range (1 to 100)
random_integers = np.random.randint(1, 101, 10)
print("\nRandom integers using np.random.randint():")
print(random_integers)

# Custom normal distribution (mean=50, std=10)
normal_data = np.random.normal(loc=50, scale=10, size=10)
print("\nNormally distributed data using np.random.normal():")
print(normal_data)

# ==============================================================================
# 2. STATISTICAL CALCULATIONS (SMALL SAMPLE)
# ==============================================================================
print("\nStatistics of Normal Distribution:")
print("Mean:", np.mean(normal_data))
print("Median:", np.median(normal_data))
print("Standard Deviation:", np.std(normal_data))
print("Minimum:", np.min(normal_data))
print("Maximum:", np.max(normal_data))

# ==============================================================================
# 3. STATISTICAL CALCULATIONS (LARGE SAMPLE SIMULATION)
# ==============================================================================
large_data = np.random.normal(loc=50, scale=10, size=1000)
print("\nStatistics of 1000 Random Values:")
print("Mean:", np.mean(large_data))
print("Standard Deviation:", np.std(large_data))
print("Minimum:", np.min(large_data))
print("Maximum:", np.max(large_data))
