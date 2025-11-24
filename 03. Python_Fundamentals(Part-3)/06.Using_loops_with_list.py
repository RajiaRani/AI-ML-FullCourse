nums = [1,2, 5, 7, 8, 10, 2,22, 34]
idx = 0
x = 10
for vals in nums:
    if(vals == x):
        print(f"x found at index = {idx}")
        break
    idx+=1