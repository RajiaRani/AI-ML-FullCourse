# Design and create an online store for Products(name, price).
# Track total products being created.
# Create a static method to calculate discount on each product based on a % parameter.

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product. count +=1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total Products in Store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Final price = {final_price}")

        
p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p2 = Product("iPad", 40_000)
p1.get_info()

Product.get_count()
p1.calc_discount(p1.price, 10)


