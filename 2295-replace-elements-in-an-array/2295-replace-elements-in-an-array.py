class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # create value to index dictionary
        indexes = dict(zip(nums, range(len(nums))))
        
        # iterate through the operations and perform the said operations
        for operation in operations:
            nums[indexes[operation[0]]] = operation[1]
            indexes[operation[1]] = indexes[operation[0]]
            del indexes[operation[0]]
        
        return nums