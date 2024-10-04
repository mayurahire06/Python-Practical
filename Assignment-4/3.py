# employee_data = ('John', 'Doe', 34, 'Developer', 'New York')
# Write a function to unpack the values of the tuple into separate variables.
# Check if the value 'Developer' is present in the tuple.
# Convert the tuple into a list and add a new element 'Full-time'.


def process_employee_data(employee_data):

    first_name, last_name, age, position, city = employee_data
    
    is_developer = 'Developer' in employee_data
    
    employee_list = list(employee_data)
    employee_list.append('Full-time')
    
    return (first_name, last_name, age, position, city, is_developer, employee_list)

employee_data = ('John', 'Doe', 34, 'Developer', 'New York')
result = process_employee_data(employee_data)

print("First Name:", result[0])
print("Last Name:", result[1])
print("Age:", result[2])
print("Position:", result[3])
print("City:", result[4])
print("Is Developer:", result[5])
print("Employee List:", result[6])
