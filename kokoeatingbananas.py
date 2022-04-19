'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


'''

class Solution:

    #Using binary search to find middle point and 
    #trying each result rather than brute forcing it

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftPointer = 1
        rightPointer = max(piles)
        
        result = rightPointer
        
        while leftPointer <= rightPointer:
            middlePoint = (leftPointer + rightPointer) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middlePoint)
            
            if hours <= h:
                result = min(result,middlePoint)
                rightPointer = middlePoint - 1
            else:
                leftPointer = middlePoint + 1
        
        return result