# Q7. Write a program that takes a string from the user and prints the number of spaces in the string

n = input("Enter the statemenet: ")
space = 0
for ch in n:
    if (ch == " "):
        space+=1
print(f"number of spaces = {space}")