def determine(data_type, a):
    if data_type == "int":
        a = int(a)
        a *= 2
        return a
    elif data_type == "real":
        a = float(a)
        a *= 1.5
        return f"{a:.2f}"
    elif data_type == "string":
        return f"${a}$"


data_type = input()
a = input()

print(determine(data_type, a))
