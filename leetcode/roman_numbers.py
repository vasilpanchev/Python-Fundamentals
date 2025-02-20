def romanToInt(s: str) -> int:
    number = 0
    for roman in s:
        if roman == "I":
            number += 1
        elif roman == "V":
            number += 5
        elif roman == "X":
            number += 10
        elif roman == "L":
            number += 50
        elif roman == "C":
            number += 100
        elif roman == "D":
            number += 500
        elif roman == "M":
            number += 1000

    return number
