# Write a Python program that takes the length and width of a rectangle as input and calculates its area and perimeter. Display the results.

def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area, perimeter = rectangle_area_perimeter(length, width)

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
