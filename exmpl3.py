class Employee:
    def __init__(self ,name ,position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def give_raise(self, amount):
        """Increase the employee's salary by a given amount"""
        self.salary += amount
    
    def get_info(self):
        """Returns formatted employee details."""
        return f"Employee: {self.name}, Position:{self.position}, salary: ${self.salary}"

#Creating employee instances
emp1 = Employee("JohnBrian","Software Engineer",75000)
emp2 = Employee("JeYBee","Disk Jockey",65000)

#Accesing instance properties
print(emp1.get_info()) #Output

#Using instance methods 
emp2.give_raise(5000)
print(emp2.get_info()) 