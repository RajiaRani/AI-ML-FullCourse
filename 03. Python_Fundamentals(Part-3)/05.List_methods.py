# Methods
# list.append(val) - add one element at the end
# list.insert(idx, val) - insert elemenet at index
# list.sort() - arranges in increasing order
# list.reverse() - reverses order



list = [1, 2, 2, 3, 4, 9, 1, 0, 1]
list.append(5)
print(f" Insert at the end of the lsit - using append : {list}")

list.insert(3, 3)
print(f"Using insert - {list}")

list.sort()
print(f"Sort the list : {list}")

list.reverse()
print(f"reverse the list: {list}")