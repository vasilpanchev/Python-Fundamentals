def is_palindrome(x: int) -> bool:
    reversed_num = int(str(x)[::-1])
    if x == reversed_num:
        return True
    else:
        return False
