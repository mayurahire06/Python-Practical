# Create a class Car with two attributes: brand and year. Write a method display_info() that prints the car's brand and year. Then, create an  object of the Car class and call the display_info() method to display the car's details. Bonus: Add an attribute for color and include it in the display_info() method!

class Car():
    brand = "Rolce-Royce"
    year = 2024
    color = "Blue"
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")

my_car = Car()
my_car.display_info()
