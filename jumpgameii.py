'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        leftPointer = 0
        rightPointer = 0
        
        while rightPointer < len(nums) - 1:
            farthestRight = 0
            for i in range(leftPointer, rightPointer + 1):
                farthestRight = max(farthestRight, i + nums[i])
            leftPointer = rightPointer + 1
            rightPointer = farthestRight
            result += 1
        return result
            