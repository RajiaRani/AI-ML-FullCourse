# given a list of tuples which info(name, subject):
# list all unique course 
# list students enrolled in English
# create dictionary (subject, set of courses)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Jack", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Jack", "English"),
    ("Charlie", "Math"),
]

# list all unique course 
unique_courses = set()
for tup in info:
    # print(tup[0])
    # print(tup[1])
    unique_courses.add(tup[1])

print(unique_courses) 

# list students enrolled in English
for name, course in info:
    if(course == "English"):
     print(name)

# create dictionary (subject, set of courses)
dict = {}
for name,course in info:
    if(dict.get(name) == None):
      dict.update({name: set()})
      dict[name].add(course)
    else:
      dict[name].add(course)
print(dict)