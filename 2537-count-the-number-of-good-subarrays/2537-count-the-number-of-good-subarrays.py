class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        good_subarrays_count = 0

        freq_count = defaultdict(int)
        pairs_count = 0
        
        left = 0
        for right in range(N):
            pairs_count += freq_count[nums[right]]
            freq_count[nums[right]] += 1

            while pairs_count >= k:
                good_subarrays_count += N - right
                
                pairs_count -= (freq_count[nums[left]] - 1)
                freq_count[nums[left]] -= 1

                left += 1
            
    
        return good_subarrays_count
                
                
        