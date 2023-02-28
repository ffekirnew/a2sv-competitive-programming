class Solution:
    def __init__(self):
        self.memo = {}
        
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            array = [0] * (rowIndex + 1)
            array[0], array[-1] = 1, 1
            
            for i in range(1, rowIndex):
                if not (rowIndex - 1) in self.memo:
                    self.memo[rowIndex - 1] = self.getRow(rowIndex - 1)

                array[i] = self.memo[rowIndex - 1][i] + self.memo[rowIndex - 1][i - 1]
            return array
                
        
        