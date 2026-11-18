from collections import defaultdict
class TwoSum:
    def __init__(self):
        self.counts = defaultdict(int)
    def add(self, number: int) -> None:
        self.counts[number] += 1
    def find(self, value: int) -> bool:
        for k in self.counts.keys():
          comp = value - k
          if comp not in self.counts:
            continue
          if comp != k:
            if comp in self.counts:
              return True
          if comp == k and self.counts[k] > 1:
            return True
        return False
