tup = (1, 2, 6, 8, 2, 2, 2, 2, 3, 5, 6)

sum = 0
for val in tup:
    sum+=val
    print(val)
print(f"Sum of values = {sum}")


# Methods
# tuple.index(val) -> returns 1st occurence index
# tuple.count(val) -> counts total occurrences

print(f"Value of 6 = {tup.index(6)}")
print(f"Count of 2 = {tup.count(2)}")


point = (10, 20)
print(point)
print(point[0])
# Note = NO .append(), .remove() - tuple cannot be changed


# create a tuple of strings
s1 = ("a", "b", "c")
# print first element
print(s1[0])
# try to add a value - error show karega
# unpack tuple into variable
