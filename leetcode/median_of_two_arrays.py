List = list


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mixed_list = sorted(nums1 + nums2)
        if len(mixed_list) % 2 == 0:
            mid = int(len(mixed_list) / 2)
            average = (mixed_list[mid - 1] + mixed_list[mid]) / 2
        else:
            mid = int(len(mixed_list) / 2)
            average = mixed_list[mid]

        return average


s = Solution()
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(s.findMedianSortedArrays(nums1, nums2))
