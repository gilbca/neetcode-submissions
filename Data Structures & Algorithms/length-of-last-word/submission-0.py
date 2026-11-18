class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        word_list = stripped.split(" ")

        last = word_list[-1]

        return len(last)