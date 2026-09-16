class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position 
    def introduce(self):
        return f"Hi, I'm {self.name} and I work as a {self.position}"
#Creating instances of employees
employee1 = Employee("Alice","Software Engineer")
employee2 = Employee("Bob","Data Scientist")

#Accessing attributes
print(employee1.name)
print(employee2.position)

#Calling the introduce method
print(employee1.introduce())
print(employee2.introduce())