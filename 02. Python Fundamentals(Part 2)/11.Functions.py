# Functions is a block of statement
def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def multi(a,b):
    print(a*b)

sum(2,2)
sub(1,2)
multi(3,2)



def Sum(a,b):
    s = a+b
    return s

ans = Sum(4,5)
print(ans)


# Example
def average(a, b, c):
    avg = (a+b+c)/3
    return avg
ans = average(3,3,3)
print(ans)

# OR 
def average(a, b, c):
    sum = a+b+c
    return sum/3
ans = average(3,3,3)
print(ans)

# Defining the dafault parameters
def find_sum(a, b=1):
    s = a+b
    return s

print(find_sum(4))