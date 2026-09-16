class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    #Instance methods  
    
    # Updates the product quantity.
    def add_product(self, amount):
        self.quantity += amount
    
    # Reduces the product quantity.  
    def remove_product(self, amount):
        self.quantity -= amount
    
    #Returns formatted product details.  
    def inventory(self):
        return f"Product: {self.name}, Price: ${self.price}, Stock: {self.quantity}"
    
#Class instances
item1 = Product("Watch","700","20")
item2 = Product("Laptop","3000","19")
item3 = Product("Phone","1500","50")

#Calling the instance methods
print(item1.inventory())
print(item2.inventory())
print(item3.inventory())

#Modify the instance properties
item1.add_product(str(20))
print(item1.inventory())
