class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        out_of_order = 0
        correct_order = sorted(heights)
        for h, o in zip(heights,correct_order):
            if h != o:
                out_of_order += 1
        return out_of_order