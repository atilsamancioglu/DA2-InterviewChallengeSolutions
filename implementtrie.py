'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        currentNode = self.root
        
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character] = Node()
            currentNode = currentNode.children[character]
        currentNode.wordFinished = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        
        for character in word:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        return currentNode.wordFinished

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        
        for character in prefix:
            if character not in currentNode.children:
                return False
            currentNode = currentNode.children[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Node:
    
    def __init__(self):
        self.children = {}
        self.wordFinished = False