# __init__Method (Called as constructor)
# constructor wo function hota hai jo kisi bhi function ko consrtuct / create karne ka kaam karta hai
# init - using for to initizalize the object
# __init__ is a special method which get called everytime when we create a object. This get called automatically - means agar hum init method nhi likhte python automatic usko run karta hai 

# def __init__(self): 
# self - means it is stroing the reference of the current instance of the class

class Student:
    def __init__(self, name, age, city):
        # print("Constructor was calling...")
        self.name = name,
        self.age = age,
        self.city = city

    def get_age(self):
        return self.age

std1 = Student("Rajia", 29, "Jalandhar")
print(std1.name)
print(std1.age)
print(std1.city)

print(std1.get_age())
print(f"Student name is {std1.name} and He/She is {std1.get_age()} year's old. He/she lives in {std1.city}")