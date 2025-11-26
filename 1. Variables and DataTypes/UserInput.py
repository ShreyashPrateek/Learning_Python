# How to take user input in Python
'''In Python, you can take input from the user using the built-in input() function.'''

# Taking string input
name = input("Enter your name: ")
print("Hello,", name)

# Taking integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Always the value of user input is String by default
# You can convert it to other data types as needed
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")