# Program 1
username = input("Enter username: ")
password = input("Enter password: ")

if(username=="admin" and password=="pass"):
    print("success")
else:
    if(username!="admin"):
        print("Incorrect username")
    else:
        print("Incorrect password")


# Program 2
age = int(input('Enter your legal age: '))
citizen = input('Are you citizen of USA ?')

if(age>=18):
    if (citizen == 'True' or citizen == 'Yes' or citizen=='true' or citizen=='yes'):
        print('You can vote')
else:
    print('Sorry! you are not eligible')



# Program 3
num = 12

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative number")


# Program 4
username = "admin"
password = "1234"
otp_verified = True

if username == "admin":
    if password == "1234":
        if otp_verified:
            print("Login successful")
        else:
            print("OTP not verified")
    else:
        print("Wrong password")
else:
    print("User not found")

        

# Program 5
price = 120
coupon = "SAVE10"
is_member = True

if price >= 100:
    if coupon == "SAVE10":
        if is_member:
            print("Extra discount for members")
        else:
            print("Normal discount")
    else:
        print("Invalid coupon")
else:
    print("Minimum 100 required")
