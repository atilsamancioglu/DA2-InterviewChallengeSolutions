'''
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]
'''

class FreqStack:

    def __init__(self):
        self.countMap = {}
        self.maxCount = 0
        self.stackMap = {}

    def push(self, val: int) -> None:
        newCountOfVal = 1 + self.countMap.get(val,0)
        self.countMap[val] = newCountOfVal
        if newCountOfVal > self.maxCount:
            self.maxCount = newCountOfVal
            self.stackMap[newCountOfVal] = []
        self.stackMap[newCountOfVal].append(val)

    def pop(self) -> int:
        valueForPop = self.stackMap[self.maxCount].pop()
        self.countMap[valueForPop] -= 1
        if not self.stackMap[self.maxCount]:
            self.maxCount -= 1
        return valueForPop