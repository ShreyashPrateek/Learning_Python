# Calculate average of three numbers using a function
def calc_avg(a,b,c):
    avg = (a + b + c) / 3
    print(avg)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

calc_avg(a,b,c)

# same ques using return and printing outside the function
def calc_avg_return(a,b,c):
    avg = (a + b + c) / 3
    return avg

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = calc_avg_return(a,b,c)
print("Average is:", average)