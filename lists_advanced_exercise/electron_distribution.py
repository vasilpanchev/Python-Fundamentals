def distribute_electrons(electrons: int) -> list:
    electron_shells = []
    shell = 1

    while electrons > 0:
        current_shell_max = 2 * shell ** 2
        if electrons - current_shell_max > 0:
            electron_shells.append(current_shell_max)
            electrons -= current_shell_max
        else:
            electron_shells.append(electrons)
            break

        shell += 1

    return electron_shells


number_of_electrons = int(input())

electron_shells = distribute_electrons(number_of_electrons)

print(electron_shells)
