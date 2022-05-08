'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's Algorithm
        slowPointer = 0
        fastPointer = 0
        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            if slowPointer == fastPointer:
                break
        
        secondSlowPointer = 0
        
        while True:
            slowPointer = nums[slowPointer]
            secondSlowPointer = nums[secondSlowPointer]
            if slowPointer == secondSlowPointer:
                return slowPointer
        
        
        '''
        O(n^2)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]
        '''