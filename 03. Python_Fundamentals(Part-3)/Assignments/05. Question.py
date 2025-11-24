# Q5. Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)

# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’) depending on the operation they want to perform on the dictionary:
# 1. - 'A' Add a student
# 2. - 'B' Update marks
# 3. - 'C' Search for a student
# 4. - 'D' Display all students and marks


students = {}

while True:
    print("\nA-Add  B-Update  C-Search  D-Display  E-Exit")
    ch = input("Enter choice: ").upper()

    if ch == 'A':
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added.")

    elif ch == 'B':
        name = input("Enter name to update: ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Marks updated.")
        else:
            print("Student not found.")

    elif ch == 'C':
        name = input("Enter name to search: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Not found.")

    elif ch == 'D':
        print("All students:", students)

    elif ch == 'E':
        break

    else:
        print("Invalid choice!")
