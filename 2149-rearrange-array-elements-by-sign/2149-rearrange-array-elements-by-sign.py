class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # create the object to be returned
        rearranged = []
        
        # create two pointers to add positive and negatives
        pos, neg = 0, 0
        
        # iterate through nums
        while pos < len(nums) or neg < len(nums):
            while neg < len(nums) and nums[neg] > 0:
                neg += 1
            while pos < len(nums) and nums[pos] < 0:
                pos += 1
            
            if len(rearranged) % 2 and neg < len(nums):
                rearranged.append(nums[neg])
                neg += 1
            elif pos < len(nums):
                rearranged.append(nums[pos])
                pos += 1            
        
        return rearranged
