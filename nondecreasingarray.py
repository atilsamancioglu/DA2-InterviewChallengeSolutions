'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changedElement = 0

        for i in range(len(nums)-1):
            #if it is already non decreasing then continue to the next loop
            if nums[i] <= nums[i+1]:
                continue
            #if this is not the case then it means that we are going to change a value
            #if we already changed before, then this is already over. we can return false
            if changedElement > 0:
                return False
            
            # if 3rd element is greater than 1st element then we are going to decrease the middle one such as [1,4,3]. then [1,4,3] becomes [1,3,3]
            #if i == 0 because it means there is no [i-1] index and we are going to get out of bounds exception
            if nums[i+1] >= nums[i-1] or i==0:
                nums[i] = nums[i+1]
            else:
                # if 3rd element is smaller than 1st element then we are going to increase the 3rd one such as [2,4,1]. then [2,4,1] becomes [2,4,4]
                nums[i+1] = nums[i]
            changedElement += 1
        return True