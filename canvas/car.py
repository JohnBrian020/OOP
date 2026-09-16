class Car:
    def __init__(self, name, model, year ,speed):
        self.name = name
        self.model = model
        self.year = year
        self.speed = speed
    
    #Increase the car's speed
    def accelerate(self, amount):
        """Increase the car's speed by a certain amount"""
        self.speed += amount
    #Instance methods
    def industry(self):
        return f"This is a {self.name}, it's a {self.model} from the year {self.year} and has a top speed of {self.speed}mph"
    
#Class instances
vehicle1 = Car("Cadillac","Escalade V", 2026 ,120)   
vehicle2 = Car("Ford","Raptor F-150", 2026, 110) 

#Call instance methods
print(vehicle1.industry())  
print(vehicle2.industry()) 

#Modify the instance
vehicle2.accelerate(50)
print(vehicle2.industry())