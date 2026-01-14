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


# Remove user id
user_id = [101, 102, 101, 103, 104, 101, 102, 105, 106]
unique_users = set(user_id)
print(unique_users)

# Unique Vocabulary in NLP
text = "AI is the future of AI"
vocab = set(text.split())
print(vocab)

# Feature Selection
selected_features = {"age", "salary", "experience"}
important_features = {"salary", "experience"}
print(selected_features & important_features)

# Set Operations
A = {1,2,3}
B = {3, 4, 5}
print(A | B) # print union
print(A & B) # print Intersection
print(A - B) # Difference