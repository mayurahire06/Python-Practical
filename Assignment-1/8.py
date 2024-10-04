# Write a Python program that converts temperature from Celsius to Fahrenheit and vice versa. The program should ask the user for the temperature value and the unit (Celsius or Fahrenheit)
# and then perform the conversion.


temperature = float(input("Enter the temperature value: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == 'C':
    fahrenheit = (temperature * 9 / 5) + 32
    print(temperature, "degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit.")
elif unit == 'F':
    celsius = (temperature - 32) * 5 / 9
    print(temperature, "degrees Fahrenheit is equal to", celsius, "degrees Celsius.")
else:
    print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
