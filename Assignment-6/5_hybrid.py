# Hybrid Inheritance (combination of hierarchical and multiple inheritance)

class Engine:
    def start(self):
        print("Engine starts")

class Vehicle:
    def drive(self):
        print("Vehicle drives")

class Car(Vehicle, Engine):
    def honk(self):
        print("Car honks")

class Bike(Vehicle):
    def ring_bell(self):
        print("Bike rings bell")

car = Car()
car.start()    
car.drive()    
car.honk()     

bike = Bike()
bike.drive()   
bike.ring_bell()  
