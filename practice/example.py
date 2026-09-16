#Reminder

class Student:
    def __init__(self, name, course, registration):
        self.name = name
        self.course = course
        self.registration = registration
        
    def add_student(self):
        return f"{self.name} ,registraton no .{self.course}is enrolled to {self.registration}"
    
    def view_student(self):
        return f"{self.name}"
    
std1 = Student("John","DIPLOMA IN COMPUTER SCIENCE", "A001")
std2 = Student("kennedy","DEGREE IN ACTURIAL SCIENCE","A101")

print(std1.add_student())
print(std2.add_student())