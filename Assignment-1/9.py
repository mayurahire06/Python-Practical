# Write a Python program that calculates the Body Mass Index (BMI) based on user input for weight (in kg) and height (in meters). The formula
#  for BMI is weight / (height ** 2). Display the BMI and categorize it as underweight, normal weight, overweight, or obese.


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("You are classified as:", category)
