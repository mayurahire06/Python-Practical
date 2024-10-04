# Write a Python function multiply(a, *args) that multiplies a fixed argument a with a variable number of additional arguments. Return the product.

def multiply(a, *args):
    product = a
    for number in args:
        product *= number
    return product

print(multiply(2, 3, 4))          
print(multiply(5, 1, 2, 3))       
print(multiply(10))              
print(multiply(3, 0, 2, 4))     
print(multiply(7, 1, 1, 1, 1))    
