# first parameter is cls
# class attributes do not access the instance attributes
# also using decorates - @classmethod - change the behaviour


class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} storage space with {self.storage_type}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")
        
l1.get_info()
Laptop.get_storage_type()