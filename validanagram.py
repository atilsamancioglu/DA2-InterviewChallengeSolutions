'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t) # Time-> O(nlogn) Space -> O(1)
        
        if len(s) != len(t):
            return False
        
        letterCounts = dict()
        
        for letter in s:
            if letter in letterCounts:
                letterCounts[letter] += 1
            else:
                letterCounts[letter] = 1
                
        for letter in t:
            if letter in letterCounts:
                letterCounts[letter] -= 1
            else:
                letterCounts[letter] = 1
        
        for letter in letterCounts:
            if letterCounts[letter] != 0:
                return False
            
        return True
    
    #Time -> O(n) , Space->O(n)