'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseRecursive(s, 0, len(s)-1)
        
    def reverseRecursive(self,s:List[str], start:int,end:int):
        if start > end:
            return
        (s[start],s[end]) = (s[end],s[start])
        self.reverseRecursive(s,start+1,end-1)