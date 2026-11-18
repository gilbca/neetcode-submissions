class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        total = sum(int(d) for d in str(min(nums)))
        return int(total % 2 == 0)