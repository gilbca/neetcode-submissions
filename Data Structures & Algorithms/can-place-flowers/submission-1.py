class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left, right, count, length = 0, 0, 0, len(flowerbed)
        
        for i in range(0,length):
            spot = flowerbed[i]
            
            if i != 0:
                left = flowerbed[i-1]
            else:
                left = None
            
            if i < length-1:
                right = flowerbed[i+1]
            else:
                right = None

            if spot == 0:
                if (left == 0 or left == None) and (right == 0 or right == None):
                    flowerbed[i] = 1
                    count += 1
        return count >= n