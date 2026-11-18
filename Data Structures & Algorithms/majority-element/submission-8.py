from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        maj = n // 2
        for key, val in counter.items():
            if val > maj:
                return key