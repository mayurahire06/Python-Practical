# Create a lambda function to check if a string starts with the letter 'A'.
# Example: (lambda s: s[0].lower() == 'a')('Apple') should return True.

check_start = lambda s: s[0].lower() == 'a'

result1 = check_start('Apple')
result2 = check_start('Banana')

print(result1)  
print(result2)  
