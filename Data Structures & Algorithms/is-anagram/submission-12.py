from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        sCount = Counter(s)
        tCount = Counter(t)

        for k, v in sCount.items():
            if tCount[k] != v:
                return False
        return True