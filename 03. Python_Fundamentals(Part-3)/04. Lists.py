# Lists-
# mutable sequence of values


# A list is a collection of items.
# It can store different types of data together.
# Example: [10, "Rajia", 5.6, True]


# Example 
marks = [90, 67, 89, 56, 77, 99, 82]
marks[5] = 90
print(marks)
print(len(marks))

for i in range(0, len(marks)):
    print(marks[i])

list = [78, 90, 0.98, "rajia"]
print(list[1:2])

fruits = ["mango", "apple", "banana"]
print(fruits[0])
print(fruits[-1])

numbers = [10, 20, 30, 40,50]
print(numbers)
numbers.append(60) # insert at the end
numbers.insert(0, 5) # insert at the starting
print(numbers)
print(numbers[2:])


# Accuries
accuracies = [0.85, 0.90, 0.99, 0.89]
max = max(accuracies)
print("The maximum accuaries", max)


# Batch Prediction
batch_preds = [0, 1, 1, 0, 1]
for p in batch_preds:
    print("Predicted", p)


# list
nums = [1,2,3,4,5]
nums.append(100)
# remove 3
nums.remove(3)
# print the last element
print(nums[: -1])
# print all except first 2
print(nums[2: ])
print(len(nums))
# replace 4 with 40
nums[3] = 40
nums.reverse()
nums.sort()
# check if 10 is in the list
print( 10 in nums)
print(nums)
