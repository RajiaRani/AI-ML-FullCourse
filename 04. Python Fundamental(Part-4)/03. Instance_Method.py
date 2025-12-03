class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} storage space with {self.storage_type}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")
        
l1.get_info()