grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_sorted = sorted(student)
new_dict = {student_sorted[0]: sum(grades[0]) / len(grades[0]),
            student_sorted[1]: sum(grades[1]) / len(grades[1]),
            student_sorted[2]: sum(grades[2]) / len(grades[2]),
            student_sorted[3]: sum(grades[3]) / len(grades[3]),
            student_sorted[4]: sum(grades[4]) / len(grades[4])}
print(new_dict)
