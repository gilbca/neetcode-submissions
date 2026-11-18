class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        x = min(nums)
        s = str(x)

        val = 0
        for num in s:
            num = int(num)
            val += num
        
        if val % 2 == 0:
            return 1
        else:
            return 0