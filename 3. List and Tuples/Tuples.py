# Tuples in Python
'''In Python, a tuple is a built-in data structure that allows you to store multiple items
in a single variable. Tuples are ordered, immutable (unchangeable), and can contain elements of
different data types. Tuples are defined by enclosing elements in parentheses () and
separating them with commas.'''

# Creating a tuple
coordinates = (10, 20, 30)    # tup =(10,) for single element tuple
print("Original Tuple:", coordinates)
print(coordinates[0])  # Accessing the first element
print(coordinates[-1]) # Accessing the last element

# Tuple Slicing
subtuple = coordinates[1:3]  # Slicing from index 1 to 2
print("Sliced Tuple (1 to 2):", subtuple)

