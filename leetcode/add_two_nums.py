'''def add_two_numbers(l1: list, l2: list) -> list:
    number1 = ""
    number2 = ""

    for digit in l1:
        number1 += str(digit)

    for digit in l2:
        number2 += str(digit)

    result = list(str(int(number1) + int(number2)))

    return result


l1 = list(map(int, input()))
l2 = list(map(int, input()))

print(add_two_numbers(l1, l2))'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):A
#         self.val = val
#         self.next = next

