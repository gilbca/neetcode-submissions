from itertools import groupby

class Solution:
    def isDecomposable(self, s: str) -> bool:
        pair_found = False
        
        for _, g in groupby(s):
            length = len(list(g))
            rem = length % 3
            if rem == 0:
                continue
            elif rem == 2:
                if not pair_found:
                    pair_found = True
                else:
                    return False
            else:
                return False
        
        return pair_found