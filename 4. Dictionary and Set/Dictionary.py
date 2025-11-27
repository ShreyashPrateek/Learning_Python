# Dictionary in Python
# Dictionary are used to store data values in Key:Value pair
# They are unordered, mutable and does not allow duplicate keys

# Example
info = {
    "name" : "Shreyash", # Key:Value
    "age" : 25,
    "Subjects" : ["Python", "Java", "C++"],
    "is_adult" : True
}
print(type(info))
print(info)

info["age"] = 26
print(info)