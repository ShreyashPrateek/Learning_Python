''' Pattern Printing Problem 2
*
**
***
'''

n = int(input("Enter the number of rows for the pattern: "))    
for i in range(n):  # Outer loop for number of rows
    for j in range(i+1):  # Inner loop for number of columns 
        print("*", end="")  # Print star without newline
    print()  # Move to the next line after printing one row