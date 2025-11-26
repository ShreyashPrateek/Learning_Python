# String Functions in Python
'''Python provides several built-in string functions that allow you to manipulate and work with strings effectively.'''

# Example string
example_str = " hello, Shreyash! Welcome to Python programming. "

# strip() - Removes leading and trailing whitespace
stripped_str = example_str.strip()
print("Stripped String:", stripped_str)

# ends with() - Checks if the string ends with a specified suffix
ends_with_python = stripped_str.endswith("programming.")
print("Ends with 'programming.':", ends_with_python)

# capitalize() - Capitalizes the first character of the string
capitalized_str = stripped_str.capitalize()
print("Capitalized String:", capitalized_str)
print("Original String after capitalize():", stripped_str)  # Original string remains unchanged

# replace() - Replaces occurrences of a substring with another substring
replaced_str = stripped_str.replace("Shreyash", "Prateek") # Replacing 'Shreyash' with 'Prateek'
print("Replaced String:", replaced_str)

# find() - Finds the first occurrence of a substring and returns its index
index_of_python = stripped_str.find("Python")
print("Index of 'Python':", index_of_python)
print("Index of 'Java':", stripped_str.find("Java"))  # Returns -1 if not found

# count() - Counts the occurrences of a substring
count_of_o = stripped_str.count("o")   
print("Count of 'o':", count_of_o)