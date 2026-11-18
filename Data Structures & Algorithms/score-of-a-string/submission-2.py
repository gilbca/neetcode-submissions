class Solution:
    def scoreOfString(self, s: str) -> int:
        asc = [ord(c) for c in s]
        
        length = len(asc)

        i = 0
        total = 0
        while i+1 < length:
            total += abs(asc[i+1] - asc[i])
            i += 1
        return total