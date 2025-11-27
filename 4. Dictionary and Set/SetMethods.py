# Methonds in Set

my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# pop() removes a random element from the set
my_set.pop()
print("Set after popping an element:", my_set)

# clear() removes all elements from the set
my_set.clear()
print("Set after clearing all elements:", my_set)

# union() returns a new set with all elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# intersection() returns a new set with common elements from both sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)