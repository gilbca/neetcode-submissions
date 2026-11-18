class Solution:
    def scoreOfString(self, s: str) -> int:
        ord_s = []
        for c in s:
            ord_s.append(ord(c))
        out = 0

        for i in range(0,len(ord_s)-1):
            n1 = ord_s[i]
            n2 = ord_s[i+1]
            if n1 >= n2:
                out += n1 - n2
            else:
                out += n2 - n1
        return out
            
