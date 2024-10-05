# Create a class Employee with attributes like name, position, and salary. Use the constructor (__init__()) to initialize the attributes when an object is created. Write a method to display employee details.

class Employee():

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee position: {self.position}")
        print(f"Employee Salary: {self.salary}")
        
emp = Employee("ABC", "Manager", 70000)
emp.display_info()