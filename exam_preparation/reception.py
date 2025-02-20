employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
waiting = int(input())
total_students_helped_per_hour = employee_1 + employee_2 + employee_3
hours = 0
while waiting > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    waiting -= total_students_helped_per_hour

print(f"Time needed: {hours}h.")
