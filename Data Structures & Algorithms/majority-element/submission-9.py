from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = Counter(nums)

        return max(num_count, key=num_count.get)