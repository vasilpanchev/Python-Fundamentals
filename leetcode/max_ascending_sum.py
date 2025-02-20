class Solution:
    def max_ascending_sum(self, nums: list[int]) -> int:
        max_sums = []
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sums.append(current_sum)
                current_sum = nums[i]

        max_sums.append(current_sum)

        return max(max_sums)


s = Solution()
numbers = list(map(int, input().split(',')))
print(s.max_ascending_sum(numbers))
