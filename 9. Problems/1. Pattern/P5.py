''' Pattern Printing Problem 5
***
 **
  *
'''

n = int(input("Enter the number of rows for the pattern: "))    
for i in range(n):  # Outer loop for number of rows 
    for j in range(i):  # Inner loop for spaces
        print(" ", end="")  # Print space without newline
    for k in range(n-i):  # Inner loop for stars
        print("*", end="")  # Print star without newline
    print()  # Move to the next line after printing one row