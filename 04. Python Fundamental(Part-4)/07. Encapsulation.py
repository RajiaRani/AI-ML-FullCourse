class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        # self._balance = balance # protected
        self.__balance = balance # private - data mangling


    def get_balance(self): # getter function
        return self.__balance
    
    def set_balance(self, newBalance): # setter function - to set the value to another value
        self.__balance = newBalance

acc1 = BankAccount("Rajia Rani", 1000000)
# print(acc1.name, acc1._balance)
print(acc1.name, acc1.__balance)
        