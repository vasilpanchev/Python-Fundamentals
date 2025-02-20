def multiply_print(text: str, times_to_repeat: int):
    if times_to_repeat > 0:
        return f"{text}{multiply_print(text, times_to_repeat - 1)}"
    else:
        return ""


string_to_multiply = input()
times_to_multiply = int(input())

print(multiply_print(string_to_multiply, times_to_multiply))
