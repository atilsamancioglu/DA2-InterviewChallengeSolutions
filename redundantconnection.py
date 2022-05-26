'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = []
        
        for i in range(len(edges) + 1):
            parents.append(i)

        ranks = [1] * (len(edges) + 1)
        
        def find(n):
            parent = parents[n]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent
        
        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)
            
            if parent1 == parent2:
                return False
            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]