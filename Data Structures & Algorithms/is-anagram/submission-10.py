from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for cs, ct in zip(sorted_s, sorted_t):
            if cs != ct:
                return False
        return True