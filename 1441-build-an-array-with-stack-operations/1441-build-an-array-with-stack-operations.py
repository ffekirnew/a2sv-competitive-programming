"""
Notes:
- only have two operations: push & pop
- Make an array equal to another array


Solution Steps:
1. Initialize the result array
2. Set an index pointer at the start of the target array
3. Start reading the stream of numbers using a loop
    3.1. If the index is out of bounds, stop the loop
    3.2. If the number is what we need right now, add "push" to result array move the index pointer on the target by one
    3.3. If the number is not what we need, add both "push" & "pop" and continue
n. Return the result array
"""

class BuildAnArrayWithStackOperations:
    def __init__(self, target: List[int], n: int):
        self.target = target
        self.n = n
    
    def solve(self):
        result = []
        
        index = 0
        for number in range(1, self.n + 1):
            if index == len(self.target):
                break
            
            result.append("Push")
            if number != self.target[index]:
                result.append("Pop")
            else:
                index += 1
        
        return result


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        solution = BuildAnArrayWithStackOperations(target, n)
        return solution.solve()
        