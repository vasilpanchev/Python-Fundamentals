courses = {}
command = input()
while command != "end":
    courses_name, student_name = command.split(" : ")
    if courses_name not in courses:
        courses[courses_name] = []
    courses[courses_name].append(student_name)
    command = input()

for (course, students) in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
