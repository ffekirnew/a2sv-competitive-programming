class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # create the object to be returned
        to_delete = 0
        
        # iterate over the strs and find the unsorted ones
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if ord(strs[row][col]) < ord(strs[row - 1][col]):
                    to_delete += 1
                    break
                               
                
        
        return to_delete
        