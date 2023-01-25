class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        
        # sort the list
        nums.sort()
        
        # set up two pointers
        left = 0
        right = len(nums) - 1
        
        # loop through and find all k sum pairs
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                answer += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return answer