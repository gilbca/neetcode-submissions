class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        move_index = {}

        for i, k in enumerate(keyboard):
            move_index[k] = i
        total = 0
        current_pos = 0
        for i, c in enumerate(word):
            total += abs(current_pos - move_index[c])
            current_pos = move_index[c]
        return total
        
        
