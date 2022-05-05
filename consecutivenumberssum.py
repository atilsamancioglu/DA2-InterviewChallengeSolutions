'''
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

'''

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0 
        
        i = 1
        
        while (n > 0):
            n -= i
            if n%i == 0:
                count += 1
            i += 1        
        return count