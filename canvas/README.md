# Python OOP Examples

## About

This project contains simple Python examples that demonstrate the basics of **Object-Oriented Programming (OOP)**.

The examples show how to:

* Create classes
* Create objects
* Add properties to objects
* Create methods
* Use `__init__()`
* Use `self`
* Change object properties
* Format output using f-strings

## What is OOP?

OOP is a way of writing programs using **classes and objects**.

A **class** is like a blueprint, while an **object** is something created from that blueprint.

For example:

```python
class Student:
    ...
```

creates a `Student` class.

We can then create students from it:

```python
std1 = Student("JohnBrian", "Software Engineer", 4)
```

Here:

* `Student` is the class
* `std1` is the object

## Examples

### 1. Student

The `Student` class stores:

* Name
* Course
* Year

It also has an `introduce()` method that displays the student's details.

```python
std1 = Student("JohnBrian", "Software Engineer", 4)

print(std1.introduce())
```

Output:

```text
Hi, I'm JohnBrian, currently pursuing Software Engineer at year 4
```

### 2. Product

The `Product` class is used to represent products in an inventory.

It stores:

* Product name
* Price
* Quantity

It also has methods for adding and removing products.

```python
item1 = Product("Watch", 700, 20)

print(item1.inventory())

item1.add_product(20)
```

The quantity will change from `20` to `40`.

**Note:** Price and quantity should be numbers, not strings, when doing calculations.

Use:

```python
item1 = Product("Watch", 700, 20)
```

instead of:

```python
item1 = Product("Watch", "700", "20")
```

### 3. Employee

The basic `Employee` example shows how to create employee objects and access their information.

Each employee has:

* Name
* Position

Example:

```python
employee1 = Employee("Alice", "Software Engineer")

print(employee1.introduce())
```

Output:

```text
Hi, I'm Alice and I work as a Software Engineer
```

### 4. Employee Salary

This example adds a salary to the `Employee` class.

The `give_raise()` method can be used to increase an employee's salary.

```python
emp1 = Employee("JohnBrian", "Software Engineer", 75000)

emp1.give_raise(5000)
```

The salary changes from `$75,000` to `$80,000`.

### 5. DJ

The `DJ` class represents a DJ and stores:

* Name
* Genre
* Number of gigs

It has methods for adding gigs and changing the music genre.

Example:

```python
music1 = DJ("Friday Mashups", "Afrobeats", 10)

music1.add_gig(20)

print(music1.mixcloud())
```

The number of gigs changes from `10` to `30`.

### 6. Car

The `Car` class represents different vehicles.

It stores:

* Car name
* Model
* Year
* Speed

The `accelerate()` method increases the car's speed.

```python
vehicle1 = Car("Cadillac", "Escalade V", 2026, 120)

vehicle1.accelerate(20)
```

The speed changes from `120mph` to `140mph`.

## Important OOP Concepts

### Class

A class is a blueprint for creating objects.

```python
class Student:
```

### Object

An object is created from a class.

```python
std1 = Student("JohnBrian", "Software Engineer", 4)
```

### `__init__()`

`__init__()` is used to set up the object's properties when it is created.

```python
def __init__(self, name, course, year):
    self.name = name
    self.course = course
    self.year = year
```

### `self`

`self` refers to the current object.

```python
self.name = name
```

It allows each object to have its own information.

### Properties

Properties store information about an object.

```python
self.name
self.course
self.year
```

### Methods

Methods are functions that belong to a class.

```python
def introduce(self):
    return f"Hi, I'm {self.name}"
```

They can be used to perform actions or get information from an object.

## Basic OOP Structure

Most of the examples follow this pattern:

```python
class ClassName:

    def __init__(self, property1, property2):
        self.property1 = property1
        self.property2 = property2

    def method(self):
        # Do something
        pass


# Create an object
object1 = ClassName("Value 1", "Value 2")

# Use the method
object1.method()
```

## How to Run

Make sure Python is installed:

```bash
python --version
```

Save your Python code in a `.py` file, for example:

```text
student.py
```

Then run:

```bash
python student.py
```

## Suggested Structure

```text
python-oop-examples/
│
├── README.md
├── student.py
├── product.py
├── employee_basic.py
├── employee_salary.py
├── dj.py
└── car.py
```

## What I Learned

After going through these examples, I should be able to:

* Create a class
* Create objects
* Use `__init__()`
* Understand `self`
* Create object properties
* Create methods
* Create multiple objects from one class
* Change object properties using methods

## Next Topics

After learning these basics, the next OOP topics to learn are:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
5. Class variables
6. Class methods
7. Static methods
8. Getters and setters
9. `__str__()` and other special methods
