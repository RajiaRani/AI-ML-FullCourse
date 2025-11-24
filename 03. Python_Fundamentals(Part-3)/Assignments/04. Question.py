# Q4. Given a tuple of integers, create:
#  A tuple of all even numbers
#  A tuple of all odd numbers

tup = (1,2,3,4,5,6,7,8,9,10)
even = ()
odd = ()
for i in tup:
    if(i%2 == 0):
        even = even + (i,) # add to even tuple
    else:
        odd = odd + (i,)  # add to odd tuple

print("Even numbers:", even)
print("Odd numbers:", odd)
    