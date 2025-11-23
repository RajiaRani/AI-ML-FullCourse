# For loops using for sequential travel

# Program 1
# name = "Hello world"

# if 'o' in name:
#     print("o is present")
# in - called membership operator
# for i in name:
#     print(i)



# Program 2
# for i in range(6):
#     print(i)

# Program 3
word = "Artificial Intelligence"
count = 0
for ch in word:
    if (ch == 'l'):
        count+=1
print(count)



# Program 4 - print vowel - a, e, o, u, i
vowel_count = 0
for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or  ch=='u'):
        vowel_count+=1
print(vowel_count)
