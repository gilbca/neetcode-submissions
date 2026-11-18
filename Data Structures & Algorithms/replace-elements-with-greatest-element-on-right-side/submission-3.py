class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = []

        i = 0

        while i+1 < len(arr):
            curr = max(arr[i+1:])
            output.append(curr)
            i+=1
        
        output.append(-1)
        return output

