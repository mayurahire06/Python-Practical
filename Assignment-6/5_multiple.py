# Multiple Inheritance

class Engine:
    def start(self):
        print("Engine starts")

class Wheels:
    def rotate(self):
        print("Wheels rotate")

class Car(Engine, Wheels):
    pass

car = Car()
car.start()  
car.rotate() 
