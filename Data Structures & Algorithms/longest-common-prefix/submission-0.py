class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = 201
        for c in strs:
            if len(c) < max_len:
                max_len = len(c)
        
        for i in range(0,max_len):
            char = strs[0][i]
            for word in strs:
                if word[i] != char:
                    return strs[0][:i]
        return strs[0][:max_len]


        