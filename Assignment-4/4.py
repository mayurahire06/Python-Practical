# skills_A = {'Python', 'Java', 'SQL'}
# skills_B = {'Python', 'HTML', 'CSS'}
# Write a Python program to find:
# Skills that are in both sets.
# Skills that are unique to skills_A.
# The union of both skill sets.


skills_A = {'Python', 'Java', 'SQL'}
skills_B = {'Python', 'HTML', 'CSS'}

# Skills that are in both sets (intersection)
common_skills = skills_A.intersection(skills_B)

# Skills that are unique to skills_A (difference)
unique_to_A = skills_A.difference(skills_B)

# The union of both skill sets
all_skills = skills_A.union(skills_B)

# Displaying the results
print("Skills in both sets:", common_skills)
print("Skills unique to skills_A:", unique_to_A)
print("Union of both skill sets:", all_skills)
