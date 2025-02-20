happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())

happiness = [x * happiness_improvement_factor for x in happiness]

average_happiness = sum(happiness) / len(happiness)

happy_employees = [x for x in happiness if x >= average_happiness]

count_of_happy_employees = len(happy_employees)

print(f"Score: {count_of_happy_employees}/{len(happiness)}. ", end='')
if count_of_happy_employees >= len(happiness) / 2:
    print("Employees are happy!")
else:
    print("Employees are not happy!")
