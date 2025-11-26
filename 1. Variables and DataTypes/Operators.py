# Operators in Python
'''Operators are special symbols in Python that perform operations on variables and values.'''

# Arithmetic Operators
a = 15
b = 4
print("Addition:", a + b)          # Output: Addition: 19
print("Subtraction:", a - b)       # Output: Subtraction: 11    
print("Multiplication:", a * b)    # Output: Multiplication: 60
print("Division:", a / b)          # Output: Division: 3.75
print("Floor Division:", a // b)   # Output: Floor Division: 3
print("Modulus:", a % b)           # Output: Modulus: 3
print("Exponentiation:", a ** b)   # Output: Exponentiation: 50625

print()  # Print a blank line for better readability

# Relational Operators
a = 10
b = 20
print("Equal to:", a == b)         # Output: Equal to: False
print("Not equal to:", a != b)     # Output: Not equal to: True
print("Greater than:", a > b)      # Output: Greater than: False
print("Less than:", a < b)         # Output: Less than: True
print("Greater than or equal to:", a >= b)  # Output: Greater than or equal to: False
print("Less than or equal to:", a <= b)     # Output: Less than or equal to: True

print()  # Print a blank line for better readability

# Assignment Operators
a = 10
print("Initial value of a:", a)    # Output: Initial value of a: 10
a += 5
print("After a += 5, a:", a)       # Output: After a += 5, a: 15
a -= 3
print("After a -= 3, a:", a)       # Output: After a -= 3, a: 12
a *= 2
print("After a *= 2, a:", a)       # Output: After a *= 2, a: 24
a /= 4
print("After a /= 4, a:", a)       # Output: After a /= 4, a: 6.0
a //= 2
print("After a //= 2, a:", a)      # Output: After a //= 2, a: 3.0
a %= 2
print("After a %= 2, a:", a)       # Output: After a %= 2, a: 1.0
a **= 3
print("After a **= 3, a:", a)      # Output: After a **= 3, a: 1.0

print()  # Print a blank line for better readability

# Logical Operators
a = True
b = False
print("a and b:", a and b)        # Output: a and b: False
print("a or b:", a or b)          # Output: a or b: True
print("not a:", not a)            # Output: not a: False    
print("not b:", not b)            # Output: not b: True
