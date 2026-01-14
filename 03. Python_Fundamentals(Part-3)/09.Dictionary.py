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


# Model Hyperparameters
model_config = {
    "learning_rate":0.01,
    "batch_size": 23, 
    "epcho": 10
}
print(model_config["learning_rate"])
# add
model_config["optimizer"] = "adam"
# delection
del model_config["batch_size"]
# Loop
for key, value in model_config.items():
    print(key, value)

person = {
    "name" : ["Rajia Rani", "Chenchu Reddy", "Shiva Reddy"],
    "age" : [29, 28, 1]
}
print(person["name"][0])
print(person["name"][1])
print(person["name"][2])


features = {
    "age":25,
    "salary":123456,
    "experience":2
}
print(features["age"])
print(features["salary"])
print(features["experience"])


# Label Encoding 
label_map={
    "cat":0,
    "dog": 1,
    "horse": 2
}
print(label_map["dog"])

