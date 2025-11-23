#  Break use for to terminate or end the loop
# contunue use for continue the loop

i = 1
while(i<=10):
    if(i%6 == 0):
     break
    print(i)
    i+=1

print("Outside the loop....")


# Program 2
i = 1
while(i<=10):
   if(i%3 == 0):
      i+=1
      continue
   print(i)
   i+=1
print("Outside the loop....")   

# Program 3 - ODD Numbers
i = 1
while(i<=10):
   print(i)
   i+=2

# Program 4
i = 1
while(i<=10):
   if(i%2 == 0):
      i+=1
      continue
   print(i)
   i+=1