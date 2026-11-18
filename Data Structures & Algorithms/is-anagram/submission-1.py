class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        sl = list(s)
        st = list(t)
        sl.sort()
        st.sort()
        for i, x in enumerate(sl):
            if x != st[i]:
                return False
        return True
        