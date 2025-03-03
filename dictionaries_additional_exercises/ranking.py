contests = {}
students = {}
command = input()
while command != "end of contests":
    contest, password_for_contest = command.split(":")
    if contest not in contests.keys():
        contests[contest] = password_for_contest
    command = input()

submission = input()
while submission != "end of submissions":
    submission_contest, submission_password, submission_username, submission_points = submission.split("=>")
    submission_points = int(submission_points)
    for (contest, password) in contests.items():
        if submission_contest == contest and submission_password == password:
            if submission_username not in students:
                students[submission_username] = {}
            if submission_contest not in students[submission_username].keys():
                students[submission_username][submission_contest] = 0
            if submission_points > students[submission_username][submission_contest]:
                students[submission_username][submission_contest] = submission_points
            break

    submission = input()

best_name = ""
best_points = 0
for (student, contests_dict) in students.items():
    current_student_points = 0
    for points in contests_dict.values():
        current_student_points += points
    if current_student_points > best_points:
        best_name = student
        best_points = current_student_points

print(f"Best candidate is {best_name} with total {best_points} points.")
print(f"Ranking:")
for student in sorted(students.keys()):
    print(student)
    for (contest, points) in sorted(students[student].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
