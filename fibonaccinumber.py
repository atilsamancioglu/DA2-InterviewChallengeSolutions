'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

'''

#Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

#Iterative
class Solution:
    def fib(self, n: int) -> int:
        x,y = 0,1

        for i in range(n):
            x,y = y,x+y

        return x

#Memoization - we should include a list of fib number calculations to see the effect
class Solution:
    def fib(self, n: int) -> int:
        def iterativeSolution(n):
            x,y = 0,1
            for i in range(n):
                x,y = y,x+y
            return x
        
        memo = {}

        if n not in memo:
            memo[n] = iterativeSolution(n)

        return memo[n]  
