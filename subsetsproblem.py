'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                result.append(result[i]+[num])
        return result
        

#O (n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subsetCurrent = []
        
        def dfs(index):
            #base case
            if index >= len(nums):
                result.append(subsetCurrent.copy())
                return
        
            #include nums[index]
            subsetCurrent.append(nums[index])
            dfs(index+1)
            
            #don't include nums[index]
            subsetCurrent.pop()
            dfs(index+1)
            
        dfs(0)
        return result