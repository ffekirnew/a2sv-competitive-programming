class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = set()
        
        seeker, holder = 0, 0
        
        while seeker < len(nums):
            if nums[seeker] not in seen:
                nums[holder] = nums[seeker]
                seen.add(nums[seeker])
                holder += 1
            seeker += 1
        
        return len(seen)
        