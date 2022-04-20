'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s):
            return []
        
        pDict = {}
        sDict = {}
        result = []
        
        for i in range(len(p)):
            pDict[p[i]] = 1 + pDict.get(p[i],0)
            sDict[s[i]] = 1 + sDict.get(s[i],0)
        
        
        if pDict == sDict:
            result.append(0)
        
        leftPointer = 0
        
        for rightPointer in range(len(p),len(s)):
            sDict[s[rightPointer]] = 1 + sDict.get(s[rightPointer],0)
            sDict[s[leftPointer]] -= 1
            
            if sDict[s[leftPointer]] == 0:
                sDict.pop(s[leftPointer])
            
            leftPointer += 1
            
            if sDict == pDict:
                result.append(leftPointer)
        return result