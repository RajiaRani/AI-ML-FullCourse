# Q3. Input two lists of integers from the user. Merge them into one list and sort the result.
# Eg -  list1 = [1, 2, 7] list2 = [2, 4, 5] --  result = [1, 2, 3, 54, 5, 7]


# take input lists from user
num1 = list(map(int, input("Enter numbers for list1: ").split()))
num2 = list(map(int, input("Enter numbers for list2: ").split()))


# merge
merge = num1 + num2
merge.sort()
print(merge)


