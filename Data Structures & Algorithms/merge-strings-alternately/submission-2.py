class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1Len = len(word1)
        w2Len = len(word2)
        out = []
        if w1Len > w2Len:
            for c1, c2 in zip(word1[0:w2Len], word2):
                out.append(c1)
                out.append(c2)
            out.extend(list(word1[w2Len:]))
        else:
            for c1, c2 in zip(word1, word2[0:w1Len]):
                out.append(c1)
                out.append(c2)
            out.extend(list(word2[w1Len:]))
        
        return "".join(out)