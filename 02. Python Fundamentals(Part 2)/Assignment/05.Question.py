# Write a function that returns the sum of digits

n = int(input("Enter the numbers: "))
def cal_sum(n):
    sum = 0
    while(n>0):
        sum+=n%10
        n = n//10
        return sum
    
print(cal_sum(n))
