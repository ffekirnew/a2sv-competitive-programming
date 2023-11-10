class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        good_subarrays_count = 0

        freq_count = defaultdict(int)
        pairs_count = 0
        
        left = 0
        for right, number in enumerate(nums):
            pairs_count += freq_count[number]
            freq_count[number] += 1

            while pairs_count >= k:
                good_subarrays_count += N - right
                
                left_number = nums[left]
                pairs_count -= (freq_count[left_number] - 1)
                freq_count[left_number] -= 1

                left += 1
    
        return good_subarrays_count
                
                
        