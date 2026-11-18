class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
      num_freq = Counter(nums)
      return max((n for n, freq in num_freq.items() if freq == 1), default = -1)
        