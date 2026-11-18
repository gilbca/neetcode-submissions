class Solution:

    def isValid(self, s: str) -> bool:
        opening = ["(","{","["]
        closing = [")","}","]"]
        stack = []
        
        for char in s:
            if char in closing:
                c_index = closing.index(char)
                if stack and c_index == opening.index(stack[-1]):
                    stack.pop(-1)
                else:
                    return False
            if char in opening:
                stack.append(char)
        return not stack





        