'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        bt = [amount + 1] * (amount + 1)
        bt[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    bt[a] = min(bt[a],1+bt[a-coin])
        
        if bt[amount] == amount + 1:
            return -1
        else:
            return bt[amount]