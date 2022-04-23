'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textHashMap = {}
        for character in text:
            if textHashMap.get(character) != None:
                textHashMap[character] = textHashMap[character] + 1
            else:
                textHashMap[character] = 1
        
        balloonHashMap = {"b": 1, "a" : 1, "l" : 2, "o" : 2, "n" : 1}
        
        result = len(text)
        
        for c in balloonHashMap:
            result = min(result, textHashMap.get(c,0) // balloonHashMap.get(c,0))
            
        return result