from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums.sort(reverse=True)

        i = 0
        max_n = -1
        for n in nums:
            if n > max_n and c[n] < 2:
                max_n = n
        return max_n