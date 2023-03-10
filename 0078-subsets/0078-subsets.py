class Solution:
    def backtrack(self, index=0, array=[]):
        if index == len(self.nums):
            self.subsets_collection.add(tuple(array))
        if index >= len(self.nums):
            return
        
        array.append(self.nums[index])
        self.backtrack(index + 1, array)
        array.pop()
        self.backtrack(index + 1, array)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # create the object to be returned
        self.subsets_collection = set()
        
        # formulate the solution
        self.nums = nums
        self.backtrack()

        # return the solution
        return self.subsets_collection
        