# WAP to check if list contains palindrome of elements

# Hint : A palindrome is a sequence that reads the same backward as forward.
# Hint : Use copy()

list1 = [1,2,3,2,1]
list2 = [1,2,3,4,5]

copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print("List1 is a Palindrome")
else:
    print("List1 is not a Palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if list2 == copy_list2:
    print("List2 is a Palindrome")
else:
    print("List2 is not a Palindrome")

