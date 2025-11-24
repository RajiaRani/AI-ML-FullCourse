# Q9. Given a list, print all elements that appear more than once in the list.

num = [1, 2, 2 , 2, 2, 2, 4, 5, 6, 7, 8, 3, 5, 7, 2, 6,2]
seen = set()
duplicate = set()

for i in num:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)

print("Repeated elements:", duplicate)