steps_as_strings = input().split(' ')
middle = int(len(steps_as_strings) / 2) + 1
steps = []

for step in steps_as_strings:
    steps.append(int(step))

left = 0
right = 0

for i in range(middle - 1):
    left += steps[i]
    if steps[i] == 0:
        left *= 0.8

for i in range(len(steps) - 1, middle - 1, -1):
    right += steps[i]
    if steps[i] == 0:
        right *= 0.8

if left < right:
    print(f"The winner is left with total time: {left:.1f}")
else:
    print(f"The winner is right with total time: {right:.1f}")
