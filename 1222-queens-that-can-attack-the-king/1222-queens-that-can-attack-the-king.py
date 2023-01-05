class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # create the object to be returned
        queens_directly_attacking_king = []
        
        # change the queens list to a set for an O(1) lookup
        queens = set(map(tuple, queens))
        
        # create the directions to look at
        directions = ['N', 'E', 'W', 'S', 'NE', 'NW', 'SE', 'SW']
        
        # iterate through the directions and find all queens that can attack the king
        for direction in directions:
            current_square = king[:]
            while 0 <= current_square[0] <= 7 and  0 <= current_square[1] <= 7:
                if tuple(current_square) in queens:
                    queens_directly_attacking_king.append(current_square)
                    break
                else:
                    if 'N' in direction:
                        current_square[0] -= 1
                    elif 'S' in direction:
                        current_square[0] += 1
                    if 'E' in direction:
                        current_square[1] += 1
                    elif 'W' in direction:
                        current_square[1] -= 1

        return queens_directly_attacking_king
        