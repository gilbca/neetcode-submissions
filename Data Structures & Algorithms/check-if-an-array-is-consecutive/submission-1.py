class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        else:
            mn = min(nums)
            mx = max(nums)

            return mx - mn == len(nums) - 1