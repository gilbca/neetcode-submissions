class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation = {
            "0": "0",
            "1": "1",
            "2": "-1",
            "3": "-1",
            "4": "-1",
            "5": "-1",
            "6": "9",
            "7": "-1",
            "8": "8",
            "9": "6"
            }

        nums = str(n)
        nums = list(nums[::-1])
        flipped = []
        for num in nums:
            if rotation[num] == "-1":
                return False
            else:
                flipped.append(rotation[num])

        flipped = "".join(flipped)

        flipped_n = int(flipped)

        if flipped_n == n:
            return False
        else:
            return True
