# Loops in Python
# A loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

'''While Loop
The while loop in Python is used to execute a block of statements repeatedly as long as given condition is true.'''
# Syntax:
# while condition:
#     :code block to be executed

# While loop example
count = 1
while count <= 5:
    print(count, ". Shreyash")
    count += 1  # Increment count by 1

print("Loop ended")
# Q : Print numbers from 1 to 5 using while loop
num = 1
while num <= 5:
    print(num) 
    num += 1 

print("End of while loop examples")

# Q : Print numbers from 5 to 1 using while loop
num = 5
while num >= 1:
    print(num)
    num -= 1

print("End of while loop examples")

# Q : Print multiplication table of number n
num = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(num * i)
    i += 1

print("End of multiplication table")

# Q : Print the elements of a list using while loop
fruits = ["apple", "banana", "cherry", "date"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

print("End of list printing")

# Search for an element in a tuple using while loop
numbers = (10, 20, 30, 40, 50)
num_to_find = int(input("Enter a number to search in the tuple: "))
i = 0
while i < len(numbers):
    if numbers[i] == num_to_find:
        print("Number found at index:", i)
        break
    i += 1