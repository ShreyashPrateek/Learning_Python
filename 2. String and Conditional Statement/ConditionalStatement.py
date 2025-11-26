# Conditional Staements in Python
# if-else
# if-elif-else
# Nested if-else
# if-elif ladder

# Example of if-else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example of if-elif-else
marks = int(input("Enter your marks: "))        
if marks >= 90:
    print("Grade: A")
    print("Excellent performance!")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")