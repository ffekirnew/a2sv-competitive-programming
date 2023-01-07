class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # create the object to be returned
        operations = []
        
        # store where ones are found
        ones_indexes = []
        for idx, box in enumerate(boxes):
            if box == '1':
                ones_indexes.append(idx)
        
        # collect the answers
        for idx in range(len(boxes)):
            answer = 0
            for one_idx in ones_indexes:
                answer += abs(idx - one_idx)
            
            operations.append(answer)
        
        return operations
        
        
        