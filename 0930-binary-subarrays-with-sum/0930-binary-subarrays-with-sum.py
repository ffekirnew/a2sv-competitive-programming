class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        answer = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0
        
        for i, num in enumerate(nums):
            curr += num
            
            if curr - goal in prefix:
                answer += prefix[curr - goal]
            
            prefix[curr] += 1
        
        return answer