# OOP
# Python OOP Examples

## 📌 Overview

This project contains a collection of simple Python examples demonstrating the fundamentals of **Object-Oriented Programming (OOP)**.

The examples show how to:

* Create classes
* Create objects (instances)
* Define instance properties
* Use the `__init__()` constructor
* Create instance methods
* Access object properties
* Modify object properties
* Use methods to perform actions on objects
* Use **f-strings** to format output

---

## 🧠 What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming approach that organizes code around **objects**.

An object contains:

* **Properties/Attributes** → Data that describes the object
* **Methods** → Functions that define what the object can do

For example, a `Student` object can have:

```python
name
course
year
```

and can perform an action such as:

```python
introduce()
```

---

# 📚 Examples Included

## 1. Student Class

The `Student` class demonstrates how to create student objects with different properties.

### Properties

```python
self.name
self.course
self.year
```

### Method

```python
introduce()
```

The method returns a formatted introduction containing the student's name, course, and year.

### Example

```python
std1 = Student("JohnBrian", "Software Engineer", 4)
std2 = Student("William", "Mechanical Engineer", 3)

print(std1.introduce())
```

### Expected Output

```text
Hi, I'm JohnBrian, currently pursuing Software Engineer at year 4
```

---

# 2. Product Class

The `Product` class demonstrates how objects can contain inventory information and how their properties can be modified using methods.

### Properties

```python
self.name
self.price
self.quantity
```

### Methods

```python
add_product()
remove_product()
inventory()
```

`add_product()` increases the product quantity.

```python
def add_product(self, amount):
    self.quantity += amount
```

`remove_product()` decreases the product quantity.

```python
def remove_product(self, amount):
    self.quantity -= amount
```

`inventory()` returns the product information in a formatted string.

```python
return f"Product: {self.name}, Price: ${self.price}, Stock: {self.quantity}"
```

### Example

```python
item1 = Product("Watch", 700, 20)

print(item1.inventory())
```

### Expected Output

```text
Product: Watch, Price: $700, Stock: 20
```

### ⚠️ Important Note

The values for `price` and `quantity` should ideally be stored as **numbers**, rather than strings.

Use:

```python
item1 = Product("Watch", 700, 20)
```

instead of:

```python
item1 = Product("Watch", "700", "20")
```

This is important because mathematical operations such as:

```python
self.quantity += amount
```

work correctly with integers.

For example:

```python
item1.add_product(20)
```

will change the stock from:

```text
20 → 40
```

---

# 3. Employee Class — Basic

This example demonstrates how to create employee objects and access their properties.

### Properties

```python
self.name
self.position
```

### Method

```python
introduce()
```

### Example

```python
employee1 = Employee("Alice", "Software Engineer")
employee2 = Employee("Bob", "Data Scientist")

print(employee1.name)
print(employee2.position)

print(employee1.introduce())
print(employee2.introduce())
```

### Expected Output

```text
Alice
Data Scientist
Hi, I'm Alice and I work as a Software Engineer
Hi, I'm Bob and I work as a Data Scientist
```

This example demonstrates that each object can have its own unique data even though both objects come from the same class.

---

# 4. Employee Class — Salary Management

This example expands on the basic `Employee` class by adding a salary property.

### Properties

```python
self.name
self.position
self.salary
```

### Methods

```python
give_raise()
get_info()
```

The `give_raise()` method modifies the employee's salary.

```python
def give_raise(self, amount):
    self.salary += amount
```

### Example

```python
emp1 = Employee("JohnBrian", "Software Engineer", 75000)
emp2 = Employee("JeYBee", "Disk Jockey", 65000)

print(emp1.get_info())

emp2.give_raise(5000)

print(emp2.get_info())
```

### Expected Output

```text
Employee: JohnBrian, Position:Software Engineer, salary: $75000
Employee: JeYBee, Position:Disk Jockey, salary: $70000
```

This demonstrates how instance methods can **modify an object's properties**.

---

# 5. Employee Class — Introduction

This is another simple implementation of the `Employee` class.

The class contains two properties:

```python
self.name
self.position
```

and one method:

```python
introduce()
```

### Example

```python
employee1 = Employee("JohnBrian", "Software Engineer")
employee2 = Employee("JeYBee", "Disk Jockey")

print(employee1.introduce())
print(employee2.introduce())
```

### Expected Output

```text
Hi, I'm JohnBrian, I work as a Software Engineer
Hi, I'm JeYBee, I work as a Disk Jockey
```

This example reinforces the basic relationship between **classes, objects, properties, and methods**.

---

# 6. DJ Class

The `DJ` class demonstrates how an object can have properties that change during program execution.

### Properties

```python
self.name
self.genre
self.gig
```

### Methods

```python
add_gig()
changing_genre()
mixcloud()
```

### Adding Gigs

```python
def add_gig(self, amount):
    self.gig += amount
```

This allows us to increase the number of gigs.

For example:

```python
music1.add_gig(20)
```

If the DJ originally had:

```text
10 gigs
```

they will now have:

```text
30 gigs
```

### Changing Genre

```python
music1.changing_genre("Amapiano")
```

This changes the DJ's genre.

### Example

```python
music1 = DJ("Friday Mashups", "Afrobeats", 10)

print(music1.mixcloud())

music1.add_gig(20)

print(music1.mixcloud())
```

### Expected Output

```text
DJ :Friday Mashups, Genre : Afrobeats, gig 10
DJ :Friday Mashups, Genre : Afrobeats, gig 30
```

---

# 7. Car Class

The `Car` class demonstrates how objects can represent vehicles and how their properties can be modified.

### Properties

```python
self.name
self.model
self.year
self.speed
```

### Methods

```python
accelerate()
industry()
```

The `accelerate()` method increases the car's speed.

```python
def accelerate(self, amount):
    self.speed += amount
```

### Example

```python
vehicle1 = Car("Cadillac", "Escalade V", 2026, 120)
vehicle2 = Car("Ford", "Raptor F-150", 2026, 110)

print(vehicle1.industry())
print(vehicle2.industry())

vehicle2.accelerate(50)

print(vehicle2.industry())
```

### Expected Output

```text
This is a Cadillac, it's a Escalade V from the year 2026 and has a top speed of 120mph
This is a Ford, it's a Raptor F-150 from the year 2026 and has a top speed of 110mph
This is a Ford, it's a Raptor F-150 from the year 2026 and has a top speed of 160mph
```

---

# 🔑 Key OOP Concepts

## 1. Class

A class is a **blueprint** for creating objects.

```python
class Student:
```

The class defines what properties and methods Student objects will have.

---

## 2. Object / Instance

An object is an individual instance created from a class.

```python
std1 = Student("JohnBrian", "Software Engineer", 4)
```

Here:

* `Student` → Class
* `std1` → Object/Instance

---

## 3. `__init__()`

The `__init__()` method initializes an object's properties when the object is created.

```python
def __init__(self, name, course, year):
    self.name = name
    self.course = course
    self.year = year
```

---

## 4. `self`

`self` refers to the **current object**.

For example:

```python
self.name = name
```

means the object's `name` property receives the value provided to the constructor.

---

## 5. Instance Properties

Instance properties store information that belongs to a specific object.

```python
self.name
self.course
self.year
```

Different objects can have different values.

```python
std1 = Student("JohnBrian", "Software Engineer", 4)
std2 = Student("William", "Mechanical Engineer", 3)
```

Both are `Student` objects, but they contain different information.

---

## 6. Instance Methods

Instance methods are functions defined inside a class that operate on objects.

Example:

```python
def introduce(self):
    return f"Hi, I'm {self.name}"
```

They can be called using an object:

```python
std1.introduce()
```

---

## 7. Modifying Object Properties

Methods can modify an object's existing properties.

For example:

```python
def accelerate(self, amount):
    self.speed += amount
```

Calling:

```python
vehicle2.accelerate(50)
```

changes the object's speed.

---

# 🏗️ General OOP Structure

Most of the examples follow this structure:

```python
class ClassName:

    def __init__(self, property1, property2):
        self.property1 = property1
        self.property2 = property2

    def method(self):
        # Perform an action
        pass


# Create objects
object1 = ClassName("Value 1", "Value 2")

# Call methods
object1.method()
```

---

# ▶️ How to Run

Make sure Python is installed on your computer.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

Save an example in a Python file, for example:

```text
student.py
```

Then run:

```bash
python student.py
```

---

# 📂 Suggested Project Structure

You can organize the examples like this:

```text
python-oop-examples/
│
├── README.md
├── student.py
├── product.py
├── employee_basic.py
├── employee_salary.py
├── employee_intro.py
├── dj.py
└── car.py
```

---

# 🎯 Learning Objectives

After completing these examples, you should understand:

* What a class is
* What an object is
* How to create classes in Python
* How to use `__init__()`
* How `self` works
* How to create instance properties
* How to create instance methods
* How to create multiple objects from one class
* How objects can contain different data
* How methods can modify object properties
* How to format output using f-strings

---

# 🚀 Next Steps

Once you are comfortable with these examples, continue learning:

1. **Encapsulation**
2. **Inheritance**
3. **Polymorphism**
4. **Abstraction**
5. Class variables
6. Static methods
7. Class methods
8. Getters and setters
9. Magic/dunder methods such as `__str__()`

These concepts will allow you to build more complete Python applications using OOP.
