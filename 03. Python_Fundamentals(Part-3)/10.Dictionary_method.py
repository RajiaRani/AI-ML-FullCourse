# d.keys() -> returns all keys
# d.values() -> returns all values
# d.items() -> returns (key, val) pairs
# d.get(val) -> returns values according to key
# d.update(new_item) -> add new item to dict


dict = {
    "name":"Rajia Rani", 
    "standard":12, 
    "subjects":["Maths", "Physics", "Chemistry", "English"],
    "marks":[89, 76, 84, 90]
}

print(f"Show all Keys = {dict.keys()}")
print(f"Show all values = {dict.values()}")
print(dict.items())
print(dict.get("subjects"))
print(dict.update({"age":25}))
print(dict)