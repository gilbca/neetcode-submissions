class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        small = min(nums)
        total = sum(int(d) for d in str(small))
        if total % 2 == 0:
          result = 1
        else:
          result = 0
        return result