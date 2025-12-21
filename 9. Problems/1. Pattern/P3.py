''' Pattern Printing Problem 3
***
**
*
'''

n = int(input("Enter the number of rows for the pattern: "))    
for i in range(n):  
    for j in range(n-i):  
        print("*", end="") 
    print()  