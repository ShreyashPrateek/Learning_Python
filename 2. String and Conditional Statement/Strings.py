# String in python
'''In Python, a string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), 
or triple quotes (''' ''' or """ """). Strings are used to represent textual data.'''

# Creating strings
single_quote_str = 'Hello, World!'
double_quote_str = "Python is fun."
triple_quote_str = '''This is a multi-line 
string in Python.'''    # Using triple quotes for multi-line strings

# Printing strings
print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)

# String concatenation
str1 = "Shreyash"
str2 = "Prateek"
concatenated_str = str1 + " " + str2 + "!"
print("Concatenated String:", concatenated_str)

# String Length
length = len(concatenated_str)
print("Length of Concatenated String:", length)

# String Indexing
first_char = concatenated_str[0]  # First character
last_char = concatenated_str[-1]   # Last character
print("First Character:", first_char)
print("Last Character:", last_char)

# String Slicing
substring = concatenated_str[0:7]  # Characters from index 0 to 6
print("Substring (0 to 6):", substring)
print("Substring (7 to end):", concatenated_str[7:len(concatenated_str)])  # From index 7 to end

# String Slice with negative step
print("Substring (-5 to -2):", concatenated_str[-5:-1])  
print("Substring (end to start):", concatenated_str[::-1])  # Reversing the string

