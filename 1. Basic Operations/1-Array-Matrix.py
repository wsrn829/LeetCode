# Accessing elements by index
element = array[index]

# Inserting elements at a specific index
array.insert(index, element)

# Removing elements at a specific index
del array[index]

# Finding the length of the array
length = len(array)

# Copying an array
new_array = array.copy()

# Sorting an array
array.sort()

# Reversing an array
array.reverse()

# Transposing a matrix
transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Multiplying two matrices
import numpy as np
result_matrix = np.dot(matrix1, matrix2)

# Finding the determinant of a matrix
import numpy as np
determinant = np.linalg.det(matrix)

# Finding the inverse of a matrix
import numpy as np
inverse_matrix = np.linalg.inv(matrix)

# Loop over array
for item in array:
    print(item)

# Find an item
if item in array:
    print("Item found")

# Insert an item
array.append(item)

# Remove an item
array.remove(item)

# Update an item
array[index] = new_item

# Swap two items
array[i], array[j] = array[j], array[i]

# Reverse an array
array.reverse()

# Sort an array
array.sort()

# Copy an array
new_array = array.copy()

# Copy part of an array
new_array = array[start:end]

# Filter an array
filtered_array = [item for item in array if condition(item)]

# Find the index of an item
index = array.index(item)

# Check if an item exists in the array
if item in array:
    print("Item exists")

# Get the first or last item in the array
first_item = array[0]
last_item = array[-1]

# Concatenate two arrays
concatenated_array = array1 + array2

# Split an array into chunks of a given size
chunks = [array[i:i+size] for i in range(0, len(array), size)]

# Flatten a multi-dimensional array
flattened_array = [item for sublist in array for item in sublist]

# Convert an array to a set or vice versa
set_array = set(array)
list_array = list(set_array)

# Convert an array to a string
string_array = ''.join(array)

# Shuffle an array
import random
random.shuffle(array)

# Merge two sorted arrays
merged_array = sorted(array1 + array2)
