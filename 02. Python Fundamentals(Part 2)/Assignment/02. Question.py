# write a function that takes two intergeers a and b and prints all even numbers between them

a = int(input('Enter the number: '))
b = int(input('Enter the number: '))

for i in range(a, b+1):
    if(i%2 == 0):
       print(i)