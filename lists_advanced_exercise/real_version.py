version = input().split('.')
version_as_integers = [int(digit) for digit in version]
version_as_integers[-1] += 1
for index in range(len(version_as_integers) - 1, 0, -1):
    if version_as_integers[index] > 9:
        version_as_integers[index] = 0
        version_as_integers[index - 1] += 1

print('.'.join([str(digit) for digit in version_as_integers]))
