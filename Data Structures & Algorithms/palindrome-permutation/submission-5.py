from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_counts = Counter(s)
        single_char_found = False
        single_char = ""
        
        odd_found = 0
        for c in char_counts.keys():
            if char_counts[c] % 2 == 1:
                if odd_found > 0:
                    return False
                else:
                    odd_found += 1
        return True

            
            
