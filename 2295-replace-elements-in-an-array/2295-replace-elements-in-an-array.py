class Solution:
    def changeDictKey(self, dictionary: dict, new_key: any, old_key: any) -> None:
        """Change a dictionary key to a new one while keeping the value.
        It is assumed the dictionary will already contain the old_key and its value.
        """
        dictionary[new_key] = dictionary[old_key]
        del dictionary[old_key]

    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # create value to index dictionary
        indexes = dict(zip(nums, range(len(nums))))
        
        # iterate through the operations and perform the said operations
        for operation in operations:
            nums[indexes[operation[0]]] = operation[1]
            
            # change the indexes dictionary to incorporate the changes
            self.changeDictKey(indexes, operation[1], operation[0])
        
        return nums