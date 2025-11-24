# Q2. Given a list of integers compute the average of all numbers in the list.

nums = [1, 2, 3, 4, 5, 6 ,7, 8]
n = len(nums)
sum = 0
for i in nums:
    sum += i

average = sum/n
print(average)