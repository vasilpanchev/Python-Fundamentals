from typing import List


def groups_of_10(nums: List[int]):
    current_group = 10
    number_of_groups = max(nums) // 10
    for i in range(number_of_groups):
        current_group_list = [num for num in nums if num <= current_group]
        nums = [num for num in nums if num not in current_group_list]
        print(f"Group of {current_group}'s: {current_group_list}")
        current_group += 10


numbers = list(map(int, input().split(', ')))
groups_of_10(numbers)
