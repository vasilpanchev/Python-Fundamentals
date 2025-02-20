targets = list(map(int, input().split()))
command = input()
count_of_shot_targets = 0
while command != "End":
    index = int(command)
    if index in range(len(targets)) and targets[index] != -1:
        shot_target_value = targets[index]
        targets[index] = -1
        count_of_shot_targets += 1
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > shot_target_value:
                    targets[i] -= shot_target_value
                else:
                    targets[i] += shot_target_value

    command = input()

print(f"Shot targets: {count_of_shot_targets} -> ", end='')
print(*targets, sep=' ')
