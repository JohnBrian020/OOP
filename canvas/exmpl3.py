#Defining the Class (class Employee): This provides the blueprint for employee objects.
class Employee:
    
    #Initializing Instance Properties (__init__): self.name, self.position, and self.salary store unique data for each employee.
    def __init__(self ,name ,position, salary):
        #Instance properties
        self.name = name
        self.position = position
        self.salary = salary
        
    #Using Instance Methods
    
    # Updates the employee's salary dynamically.
    def give_raise(self, amount):
        """Increase the employee's salary by a given amount"""
        self.salary += amount
        
    # Returns a formatted string with the employee’s details.
    def get_info(self):
        """Returns formatted employee details."""
        return f"Employee: {self.name}, Position:{self.position}, salary: ${self.salary}"

#Creating and Using Employee Instances

# creates a unique employee object.
emp1 = Employee("JohnBrian","Software Engineer",75000)
emp2 = Employee("JeYBee","Disk Jockey",65000)

#Accesing instance properties
print(emp1.get_info()) #Output

#Using instance methods 
#  modifies the object’s properties.
emp2.give_raise(5000)
print(emp2.get_info()) 