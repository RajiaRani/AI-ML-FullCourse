# Q8. Write a program to check whether two lists share no common elements.

num1 = [1, 2, 3, 5, 6]
num2 = [7, 8, 9, 10, 11]

# Changing into set
set1 = set(num1)
set2 = set(num2)

if set1.isdisjoint(set2):
    print("No common element present")
else: 
    print("Common numbers is present")