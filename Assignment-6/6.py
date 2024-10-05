# Define two classes, Engine and Body, with constructors that initialize respective attributes like horsepower and material. Then, create class Car that inherits from both Engine and Body. Use the super() method to initialize both parent class attributes from the Car class. 

'''
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Body:
    def __init__(self, material):
        self.material = material

class Car(Engine, Body):
    def __init__(self, horsepower, material):
        super().__init__(horsepower)
        Body.__init__(self, material) 

    def showDetails(self):
        print(f"Horsepower: {self.horsepower}")
        print(f"Material: {self.material}")

car = Car(250, "Aluminium")
car.showDetails()
'''

class show():
    a=10

    def details(self, a):
        print("inside function", self.a)

    print("outside function", a)

obj = show()
obj.details(20)