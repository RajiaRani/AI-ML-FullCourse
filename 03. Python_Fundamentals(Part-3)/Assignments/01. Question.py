# Q1. Ask the user for a string and check whether it is a palindrome or not.
# palindrome -- A is a string which is same when we read it forward & backward.  Eg - “madam”, “racecar” etc.
# Hint: [ - A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually. ]

# A palindrome is a word that looks the same from the front and the back.

# string = "madam"
string = input("Enter any word: ")
reverse = ""
for ch in string:
    reverse = ch+reverse

if(string == reverse):
    print("Palindrome")
else:
    print("Not Palindrome")