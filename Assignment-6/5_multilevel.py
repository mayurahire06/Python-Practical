# Multilevel Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()   
dog.walk() 
dog.bark()  
