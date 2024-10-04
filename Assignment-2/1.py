# Write a Python function area_of_rectangle(length, width) that calculates and returns the area of a rectangle. Test the function with different # # values of length and width.

def area_of_rectangle(length, width):
    return length * width

# Test cases
if __name__ == "__main__":
    test_cases = [
        (5, 10),  
        (7, 3),    
        (12.5, 4), 
        (0, 5),    
        (6, 8.5),  
    ]

    for length, width in test_cases:
        area = area_of_rectangle(length, width)
        print(f"Area of rectangle with length {length} and width {width} is: {area}")
