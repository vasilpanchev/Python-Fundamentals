def tribonacci(x):
    last3 = [0, 0, 1]
    sequence = [1]
    for i in range(x-1):
        latest = sum(last3)
        sequence.append(latest)
        last3[0], last3[1], last3[2] = last3[1], last3[2], latest

    return sequence


numbers = int(input())
tribonacci_sequence = tribonacci(numbers)
tribonacci_sequence = list(map(str, tribonacci_sequence))

print(' '.join(tribonacci_sequence))
