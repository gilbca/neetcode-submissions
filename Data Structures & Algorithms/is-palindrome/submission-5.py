class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_s = ""
        strippable = ['', '?', '!','"','.',',',' ',"'",":"]


        for c in s:
            if c not in strippable:
                strip_s += c.lower()
        rev_s = strip_s[::-1]

        print(strip_s)
        print(rev_s)

        for c, d in zip(strip_s, rev_s):
            if c != d:
                return False
        
        return True