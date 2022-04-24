'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost)-3,-1,-1): # cost -1 -> last 0 we added, cost - 2 last element(we won't update that index anyway so we better start with cost - 3). we are itirating in reverse order
            cost[i] = min(cost[i] + cost[i+1],cost[i] + cost[i+2]) # single jump or double jump
            
        return min(cost[0],cost[1])