# Formatiting means creating a dynamic strings - where we can take variables, values

# Normal formatting
a = 4
b = 2
sum = a+b
print("Sum is {}".format(sum))
print("langauge is {}".format("python"))

# index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))

# value based formatting
print("values of vars {a} & {b}".format(a=5, b=10))
print("{a} values of vars {a} & {b}".format(a=5, b=10))


# F-strings - using literal string interpulation
name = "Syal"
print(f"Hello my name is {name}")
print(f"sum of {a} and {b} is {a+b}")