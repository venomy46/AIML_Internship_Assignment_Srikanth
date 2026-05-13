#Assignment (19/02/2026)
#Assignment Name: Student Data Manager

students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)

# Calculate average
total = sum(students.values())
average = total / len(students)

# Function to assign grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

# Print results
print("\nStudent Grades:")
for name, marks in students.items():
    print(name, ":", marks, "Grade:", get_grade(marks))

print("\nTopper:", topper, "-", students[topper])
print("Class Average:", average)