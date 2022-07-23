'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
'''

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        
        products.sort()
        
        leftPointer = 0
        rightPointer = len(products) - 1
        
        for i in range(len(searchWord)):
            
            character = searchWord[i]
            
            while leftPointer <= rightPointer and (len(products[leftPointer]) <= i or products[leftPointer][i] != character):
                leftPointer += 1
            
            while leftPointer <= rightPointer and (len(products[rightPointer]) <= i or products[rightPointer][i] != character):
                rightPointer -= 1
                
            result.append([])
            
            remainingProductsCount = rightPointer - leftPointer + 1 
            
            for j in range(min(3,remainingProductsCount)):
                result[-1].append(products[leftPointer + j])
        
        return result