class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        x_min = min(nums)
        x_max = max(nums)
        diff = x_max - x_min

        n = len(nums)

        return n - 1 == diff

