'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        '''
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
        '''