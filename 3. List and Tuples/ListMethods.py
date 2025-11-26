# List Methods in Python
'''In Python, lists come with a variety of built-in methods that allow you to manipulate and    
work with lists effectively. Here are some commonly used list methods:'''

# Example list
numbers = [10, 20, 70, 40, 90]
print("Original List:", numbers)

# append() - Adds an element to the end of the list
numbers.append(60)
print("After append(60):", numbers)

# sort() - Sorts the list in ascending order
numbers.sort()
print("After sort():", numbers)

numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)

# reverse() - Reverses the order of the list
numbers.reverse()
print("After reverse():", numbers)

# insert() - Inserts an element at a specified index
numbers.insert(2, 50)  # Insert 50 at index 2
print("After insert(2, 50):", numbers)

# remove() - Removes the first occurrence of a specified element
numbers.remove(70)
print("After remove(70):", numbers)

# pop() - Removes and returns the element at the specified index (default is the last element)
popped_element = numbers.pop()
print("After pop():", numbers)
print("Popped Element:", popped_element)

