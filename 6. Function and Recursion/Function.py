# Function in Python
'''A function is a block of organized, reusable code that is used to perform a single,
related action. Functions provide better modularity for your application and a high degree of code reusing.'''

# Syntax:
# def function_name(parameters):
#     :code block to be executed
#     return value
# Function call (Not syntax but how to call a function)

# Example function
# Function definition
def cal_sum(a, b): # a,b are parameters
    sum = a + b
    print("Sum inside function:", sum) # Printing sum inside function
    return sum # Returning sum

a = int(input("Enter first number: ")) # Taking input for first number
b = int(input("Enter second number: ")) # Taking input for second number
cal_sum(a, b)  # Calling the function


# Type of function
# 1. Built-in function (print(),len(),range() etc.)
# 2. User-defined function

# 1. Built-in function
# Example of built-in function
print("Hello, World!") # print() is a built-in function
length = len("Hello") # len() is a built-in function
print("Length of 'Hello' is:", length)

# 2. User-defined function
# Example of user-defined function
def greet(name): # Function definition
    print("Hello,", name) # Printing greeting message

greet("Shreyash") # Function call