# we have 3 types of conditional statements
# if, elif, else

# Program 1
# age = 20 
# if age>=18:
#   print("You can vote")

# Program 2
# legal_age = int(input("Enter your legal age: "))
# if (legal_age >= 18):
#     print("You can vote")
# else:
#     print("Sorry you can not vote")




# Program 2
# password = int(input("Enter the password: "))
# if password == 12345:
#     print("Unlocked")
# else:
#     print("Wrong password try again!")



# Program 3
age = int(input("Enter your age: "))
if (age<13):
    print("Your are a child")
elif (age >13 and age<=18):
    print('You are a teenager')
else:
    print("You are a adult")


# Program 4
username = input("Username")
password = input("Enter password")
if(username == "admin" and password=="pass"):
    print("You login in")
elif(username != "username"):
    print("Incorrect username")
else:
    print("Incorrect password")



# Program 5
balance = 1500
withdraw = 1000
if ( balance>=withdraw):
      print("Withdrawal successful")
else:
    print("Insufficient balance")

# Program 6
marks = 82
if ( marks >= 90):
   print("Grade A")
elif(marks >= 80):
    print("Grade B")
elif(marks>=60):
    print("Grade C")
else:
    print("Grade D")


# Program 7
coupon = "SAVE10"
if coupon == "SAVE10":
    price = price * 0.90
elif coupon == "SAVE20":
    price = price * 0.80
else:
    print("Invalid coupon")
