'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for ix,num in enumerate(nums):
            nums[ix] = str(num)
            
        def customComparison(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums = sorted(nums,key=cmp_to_key(customComparison))
        
        #return "".join(nums) -> commented out because it didn't work with [0,0] ..
        return str(int("".join(nums)))