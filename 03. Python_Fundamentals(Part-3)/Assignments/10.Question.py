# Q10. Ask the user for a string and print:
# • All unique characters
# • The count of unique characters


s = input("Enter a string: ")

unique = set()

for ch in s:
    unique.add(ch)

print("Unique characters:", unique)
print("Count of unique characters:", len(unique))
