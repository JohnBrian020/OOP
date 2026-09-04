#Blueprint of the object
class Student:
    
    #Creating Instance properties
    def __init__(self, name,course, year):
        self.name = name
        self.course = course
        self.year = year
        
    #Creating instance methods
    def introduce(self):
        return f"Hi, I'm {self.name}, currently pursuing {self.course} at year {self.year}"
    
#Instance of the class
std1 = Student("JohnBrian","Software Engineer",4)
std2 = Student("William","Mechanical Engineer",3)

print(std1.introduce())