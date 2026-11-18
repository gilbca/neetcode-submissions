from itertools import groupby

class Solution:
    def isDecomposable(self, s: str) -> bool:
      pairs = 0

      for _, group in groupby(s):
          r = sum(1 for _ in group) % 3
          if r == 1:
            return False
          if r == 2:
            pairs += 1
      return pairs == 1
