class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
          return True
        elif not t:
          return False
        
        i = 0


        for j in range(0,len(t)):
            if i < len(s):
                if s[i] == t[j]:
                    i += 1
                continue
            else:
                pass
        
        return i == len(s)


