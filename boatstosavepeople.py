'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        boats = 0
        
        leftPointer = 0
        rightPointer = len(people) - 1
        
        while leftPointer <= rightPointer:
            spaceLeft = limit - people[rightPointer]
            rightPointer -= 1
            boats += 1
            if leftPointer <= rightPointer and spaceLeft >= people[leftPointer]: #leftPointer <= rightPointer because we decremented rightPointer, maybe they are equal now and if they are equal it means there is only one person left and in that case we shouldn't bother with this at all.
                leftPointer += 1
        return boats