# A set in Python is a collection of unique items.
# It does not allow duplicates
# It has no fixed order
# Sets use hashing → searching is super fast.

my_set = {1, 2, 3, 4}

s = {1, 2, 2, 3, 4}
print(s)

# Why We Use Sets? ----  To Remove Duplicates Quickly
numbers = { 1, 2, 2, 2, 2, 3, 3, 3, 5, 5 , 5, 4,4,4,4,4,4,4,4,4}
unique = set(numbers)
print(unique)


empty_set = {}
print(type(empty_set))