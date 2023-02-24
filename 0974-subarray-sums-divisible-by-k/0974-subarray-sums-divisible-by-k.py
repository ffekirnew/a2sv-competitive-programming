class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        
        answer = 0
        
        for i, num in enumerate(nums):
            nums[i] += nums[i - 1] if i > 0 else 0
            nums[i] %= k
            
            if nums[i] in freq:
                answer += freq[nums[i]]
            
            freq[nums[i]] += 1
        
        return answer
                
        