'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

'''


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differenceList = []
        for costA, costB in costs:
            differenceList.append([costB-costA,costA,costB]) #saving the original values as well
        differenceList.sort()
        result = 0
        for i in range(len(differenceList)):
            if i < len(differenceList) // 2:
                result += differenceList[i][2] #city B
            else:
                result += differenceList[i][1] #city A
        return result
