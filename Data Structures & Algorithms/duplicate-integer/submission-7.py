class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {n for n in nums}
        return not len(num_dict) == len(nums)