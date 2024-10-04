# Write a Python program that takes the principal amount, rate of interest, and time period as inputs and calculates the simple interest. 
# Display the calculated interest.

principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = (principal * rate_of_interest * time_period) / 100

print(f"The calculated simple interest is: {simple_interest}")
