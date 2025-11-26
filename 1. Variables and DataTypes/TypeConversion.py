# Type Conversion in Python
'''Type conversion is the process of converting a variable from one data type to another. '''

# Implicit Type Conversion
# Python automatically converts one data type to another without user intervention.
a = 5          # Integer
b = 2.0        # Float
c = a + b     # 'a' is converted to float
print("Implicit Type Conversion:")
print("a (int):", a)               # Output: a (int): 5
print("b (float):", b)             # Output: b (float): 2.0
print("c (float):", c)             # Output: c (float): 7.0
print("Type of c:", type(c))       # Output: Type of c: <class 'float'>


print()  # Print a blank line for better readability


# Explicit Type Conversion
# Users can explicitly convert one data type to another using built-in functions like int(), float(), str(), etc.
a = 5          # Integer
b = 2.8        # Float
print("Explicit Type Conversion:")      
print("a (int):", a)               # Output: a (int): 5
print("b (float):", b)             # Output: b (float): 2.8

# Converting float to int
c = int(b)
print("c (int) after converting b to int:", c)  # Output: c (int) after converting b to int: 2

# Converting int to float
d = float(a)
print("d (float) after converting a to float:", d)  # Output: d (float) after converting a to float: 5.0

# Converting int to string
e = str(a)
print("e (str) after converting a to str:", e)      # Output: e (str) after converting a to str: 5
print("Type of e:", type(e))                     # Output: Type of e: <class 'str'>