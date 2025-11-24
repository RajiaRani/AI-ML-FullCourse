# Write a function that returns the number of digits

n = int(input("Enter the numbers: "))

def count_digit(n):
  count = 0
  while n>0:
      count+=1
      n = n//10
  return count


print(count_digit(n))