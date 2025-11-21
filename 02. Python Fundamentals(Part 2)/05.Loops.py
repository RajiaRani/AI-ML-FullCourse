# Loops - repeat mein kam ho 
# Loops help when you want to repeat work many times automatically.

# Program 1
# while(True):
#     print("write True inside the while- means we created infinite loop. It will never stop.")


# Program 2
count = 1
while(count<=5):
    print(f"{count}. Hello world")
    count+=1

# Program 3
i = 1
while (i <= 10):
    print(i)
    i = i + 1

# Program 4:  Print even numbers 2 to 20
i = 2
while(i<=20):
    print(i)
    i = i + 2


# Program 5: Keep asking age until user enters 18+
age = int(input("Enter your age: "))
while age < 18:
    age = int(input("Age must be 18+. Enter again: "))
print("You are eligible!")


#Program 6: Add numbers until total becomes 50
total_sum = 0
while(total_sum<50):
    num = int(input('Enter number'))
    total_sum = total_sum + num
print("Total reached:", total_sum)


