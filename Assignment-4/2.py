# Create a Dictionary - student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}
# Write a Python function to find the student with the highest grade.
# Add a new student 'Eve' with a grade of 95.
# Print all the student names and their grades in alphabetical order.

def find_top_student(student_grades):
    return max(student_grades, key=student_grades.get)

student_grades = {'Ram': 85, 'Sham': 92, 'Ojas': 88, 'Anay': 79}

top_student = find_top_student(student_grades)
print("Student with the highest grade:", top_student, "with grade:", student_grades[top_student])

student_grades['Eve'] = 95

print("\nAll students and their grades in alphabetical order:")
for student in sorted(student_grades):
    print(f"{student}: {student_grades[student]}")
