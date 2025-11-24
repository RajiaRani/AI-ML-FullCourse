# write a function that prints the digits of a number(eg: n=312 -> print 3, 1, 2)

n = int(input('Enter the digit: '))
while n>0:
    digit = n%10 # right most digit
    print(digit)
    n = n//10 # remove rightmost digit