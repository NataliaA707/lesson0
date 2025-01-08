grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Biblo', 'Steve', 'Khendrik', 'Aaron'}
student_names = sorted(students)
average_grades = {}
for i, students in enumerate(student_names):
    average_grades[students] = sum(grades[i]) / len(grades[i])
print(average_grades)
