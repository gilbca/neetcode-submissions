class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        small = [nums[0], nums[1]]
        big = [nums[-2],nums[-1]]

        big_prod = big[0] * big[1]
        small_prod = small[0] * small[1]

        return big_prod - small_prod
