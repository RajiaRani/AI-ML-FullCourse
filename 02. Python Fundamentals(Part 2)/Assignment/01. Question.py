# Write a program that takes salary as input. Using conditional statemenrts, calcualte the final tax rate  based on these rules.

salary = int(input('Enter your salary'))
if(salary<30000):
    print("You will give 5% tax")
elif(salary>30000 and salary<700000):
    print("You will give 15% tax")
else:
    print("You will give 25% tax")