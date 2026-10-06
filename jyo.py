import numpy as np
import time

# 1. Array Creation, Indexing, and Slicing
matrix = np.arange(1, 21).reshape(4, 5)
print("Original 2D Matrix:\n", matrix)

sub_matrix = matrix[0:2, 1:4]
print("\nSliced Matrix (First 2 rows, columns 1-3):\n", sub_matrix)

specific_element = matrix[1, 2]
print(f"\nElement at Row 2, Column 3: {specific_element}\n")

# 2. Mathematical and Axis-wise Operations
print("Matrix squared:\n", np.square(matrix))

row_sums = matrix.sum(axis=1)    
column_means = matrix.mean(axis=0) 

print("\nSum of each row:", row_sums)
print("Mean of each column:", column_means)
print(f"Overall standard deviation: {matrix.std():.2f}\n")

# 3. Reshaping and Broadcasting
reshaped_matrix = matrix.reshape(2, 10)
print("Reshaped Matrix (2x10):\n", reshaped_matrix)

row_modifier = np.array([10, 20, 30, 40, 50])
broadcasted_result = matrix + row_modifier
print("\nBroadcasting Result (Added modifier row to every row):\n", broadcasted_result)

# 4. Save and Load Operations
np.save("numpy_explorer_data.npy", matrix)
print("\nSaved 'matrix' to 'numpy_explorer_data.npy'")

loaded_matrix = np.load("numpy_explorer_data.npy")
print("Loaded Matrix from file:\n", loaded_matrix)

# 5. Performance Comparison: NumPy vs Python Lists
size = 1_000_000  
python_list = list(range(size))
numpy_array = np.arange(size)

start_time = time.time()
python_list_squares = [x ** 2 for x in python_list]
python_duration = time.time() - start_time
print(f"\nTime taken by standard Python list: {python_duration:.5f} seconds")

start_time = time.time()
numpy_array_squares = numpy_array ** 2
numpy_duration = time.time() - start_time
print(f"Time taken by NumPy array:      {numpy_duration:.5f} seconds")

speedup = python_duration / numpy_duration
print(f"--> NumPy is approximately {speedup:.1f}x faster than standard Python lists!")