from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

      counter = Counter(nums)
      i = -1
      for k, v in counter.items():
        if k > i and v == 1:
          i = k
      return i