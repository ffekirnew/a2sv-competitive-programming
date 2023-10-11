"""
Solution Steps:
1. Initialize the starting direction and location
2. Iterate through the instructions
    2.1. If instruction is G, move forward in the direction
    2.2. Else if instruction is L or R, turn the direction
3. Return if location is the starting location or direction is changed


Complexity Analysis:
- Time Complexity: O(n)
- Space Complexity: O(1)
    where: n is number of instrictions
"""


class RobotBoundedInCircle:
    def __init__(self, instructions: str):
        self.instructions = instructions
    
    def run(self) -> bool:
        direction = 'n'
        location = [0, 0]

        dirs = {'n': ['l', 'r'], 'l': ['s', 'n'], 's': ['r', 'l'], 'r': ['n', 's']}
        movement = {'n': (0, 1), 'l': (-1, 0), 'r': (1, 0), 's': (0, -1)}
        
        for instruction in self.instructions:
            if instruction == 'G':
                location[0] += movement[direction][0]
                location[1] += movement[direction][1]
            
            elif instruction == 'L':
                direction = dirs[direction][0]
            
            elif instruction == 'R':
                direction = dirs[direction][1]
                
        return location == [0, 0] or direction != 'n'


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        solution = RobotBoundedInCircle(instructions)
        return solution.run()
        
        