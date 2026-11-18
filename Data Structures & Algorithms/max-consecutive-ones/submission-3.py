class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        final = 0
        for n in nums:
            if n == 1:
                count += 1
                if count > final:
                    final = count
            else:
                count = 0
        return final
            