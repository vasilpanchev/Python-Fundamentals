def odd_and_even_sums(a: int):
    even_sum = 0
    odd_sum = 0
    while a > 0:
        current_digit = a % 10
        if current_digit % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit

        a = int(a / 10)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_and_even_sums(number))
