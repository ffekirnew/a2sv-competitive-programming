class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # create the object to be returned
        ans = [None] * len(nums)
        
        # iterate through nums and use the given formula
        for index in range(len(nums)):
            ans[index] = nums[nums[index]]
        
        # return the solution
        return ans
        