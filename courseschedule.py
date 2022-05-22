'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                
        adjDict = {}
        
        for i in range(numCourses):
            adjDict[i] = []
        
        
        for course, prereq in prerequisites:
            adjDict[course].append(prereq)
            
        
        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                #there is a loop
                return False
            
            if adjDict[course] == []:
                return True
            
            visitSet.add(course)
            
            for prereq in adjDict[course]:
                if not dfs(prereq):
                    return False
                
            visitSet.remove(course)
            adjDict[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True