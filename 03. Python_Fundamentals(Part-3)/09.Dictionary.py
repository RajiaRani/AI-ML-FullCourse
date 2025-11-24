# stores items using KEY and VALUE
# { key1: value1, key2: value2, key3: value3 }
# Best for real-world information


dict = {
    "name":"Rajia Rani", 
    "standard":12, 
    "subjects":["Maths", "Physics", "Chemistry", "English"],
    "marks":[89, 76, 84, 90]
}

print(dict["marks"][0])
print(f"Subjects = {dict['subjects']}")