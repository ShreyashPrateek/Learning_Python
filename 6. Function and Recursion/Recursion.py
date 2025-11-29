# Recursion
# A function that calls itself to solve a smaller instance of the same problem.

# Syntax:
# def function_name(parameters):
#     if base_condition:
#         return base_value
#     else:
#         return function_name(smaller_parameters)

# printing from 5 to 1 using recursion
def print_reverse(num):
    if num < 1:  # base condition
        return
    print(num) # print the current number
    print_reverse(num - 1)  # recursive call with smaller parameter

number = int(input("Enter a number to print from that number to 1: "))
print_reverse(number)

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:  # base condition
        return 1
    else:
        return n * factorial(n - 1)  # recursive call
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print("Factorial of", num, "is:", result)