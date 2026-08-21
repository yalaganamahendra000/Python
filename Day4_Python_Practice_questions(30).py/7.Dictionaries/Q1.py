#Given students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}, find the student with the highest marks.
students={"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}

highest=0
student_name=""
for name,marks in students.items():
    if marks>highest:
        highest=marks
        student_name=name
print(highest)
print(student_name)