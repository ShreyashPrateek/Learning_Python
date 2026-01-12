''' Pattern Printing Problem 4
  *
 **
***
'''

n = int(input("Enter the number of rows for the pattern: "))    
for i in range(n):  # Outer loop for number of rows
    for j in range(n-i-1):  # Inner loop for spaces
        print(" ", end="")  # Print space without newline
    for k in range(i+1):  # Inner loop for stars
        print("*", end="")  # Print star without newline
    print()  # Move to the next line after printing one row 