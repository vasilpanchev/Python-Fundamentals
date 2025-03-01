pairs_of_rows = int(input())
students = {}
for _ in range(pairs_of_rows):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for (student, grades) in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")

