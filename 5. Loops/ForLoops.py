# For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# for loop syntax:
# for item in sequence:
#     :code block to be executed

# List example
fruits = ["apple", "banana", "cherry"]
for values in fruits:
    print(values)

number_list = [1, 2, 3, 4, 5]
for number in number_list:
    if number == 3: # searching for specific number
        print("Found",number)
        break
    print(number)


# tuple example
fruits = ("apple", "banana", "cherry")
for values in fruits:
    print(values)

# string example
for char in "banana":
    print(char)

# For loop with else
for char in "banana":
    if(char == "p"):
        print("Letter a found!")
        break
    print(char)
else:
    print("Letter a not found!")

print("\n")


# Range function
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

for i in range(5): #range(stop)
    print(i)

for i in range(1,5): #range(start, stop)
    print(i)

for i in range(1,5,2): #range(start, stop, step)
    print(i)

# multiplication tabvle using range
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(num * i)