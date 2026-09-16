class Employee:
    def __init__(self, name, position):
        #Instance Properties
        self.name = name
        self.position = position
    #Method
    def introduce(self):
        return f"Hi, I'm {self.name}, I work as a {self.position}"
#Creating new instances
employee1 = Employee("JohnBrian","Software Engineer")
employee2 = Employee("JeYBee","Disk Jockey")

#Calling the function
print(employee1.introduce())
print(employee2.introduce())
        