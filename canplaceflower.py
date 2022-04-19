'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newList = [0] + flowerbed + [0]
        
        for i in range(1,len(newList) - 1): #skip the 0s we added
            if newList[i - 1] == 0 and newList[i] == 0 and newList[i+1] == 0:
                newList[i] = 1
                n -= 1
        return n <= 0