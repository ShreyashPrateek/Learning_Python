# List in python
'''In Python, a list is a built-in data structure that allows you to store multiple items
in a single variable. Lists are ordered, mutable (changeable), and can contain elements of
different data types. Lists are defined by enclosing elements in square brackets [] and
separating them with commas.'''


# Creating a list
fruits = ['apple', 'banana', 'cherry', 'date']
print("Original List:", fruits)

# Accessing list elements
print("First Fruit:", fruits[0])  # Accessing the first element
print("Last Fruit:", fruits[-1])   # Accessing the last element 

# List Slicing
sublist = fruits[1:3]  # Slicing from index 1 to 2
print("Sliced List (1 to 2):", sublist)