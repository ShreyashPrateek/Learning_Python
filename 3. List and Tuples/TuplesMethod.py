# Methonds in Tuples
'''Tuples in Python have several built-in methods that allow you to perform various operations. 
However, since tuples are immutable, the methods available for tuples are more limited compared to lists.'''   

# Example tuple
my_tuple = (10, 20, 30, 20, 40, 50, 20)
print("Original Tuple:", my_tuple)

# count() - Returns the number of occurrences of a specified element in the tuple
count_20 = my_tuple.count(20)
print("Count of 20 in tuple:", count_20)

# index() - Returns the index of the first occurrence of a specified element in the tuple
index_30 = my_tuple.index(30)
print("Index of 30 in tuple:", index_30)

# Note: Since tuples are immutable, methods that modify the tuple (like append, remove, etc.) are not available.
# However, you can convert a tuple to a list, perform the desired operations, and then convert it back to a tuple if needed.