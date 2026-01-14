# Linear Search Implementation in Python
"Linear search (or sequential search) is the simplest search algorithm. It checks each element one by one."

"How it works:"
"1. Go through the array value by value from the start to the end."
"2. Compare each value to check if it is equal to the value we are looking for."
"3. If the value is found, return the index of that value."
"4. If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found."

"Linear Search Time Complexity: O(n), where n is the number of elements in the array."


# Simple example using 'in' keyword
mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
  print("Found!")
else:
  print("Not found!")


# Manual implementation of Linear Search
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Target found at index
    return -1  # Target not found

list1 = [3, 7, 2, 9, 5, 1, 8, 4, 6]
target = 5
result = linear_search(list1, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")


# Example with user input
def linear_search_with_input():
    n = int(input("Enter the number of elements in the list: "))
    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)
    
    target = int(input("Enter the element to search for: "))
    
    for index in range(len(arr)):
        if arr[index] == target:
            print(f"Element found at index {index}")
            return
    print("Element not found in the list")
linear_search_with_input()  


