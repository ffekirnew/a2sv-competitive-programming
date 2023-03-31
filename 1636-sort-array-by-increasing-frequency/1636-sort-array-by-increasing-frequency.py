class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        
        nums = list(zip(nums, [freq[num] for num in nums]))
        
        nums.sort(key=lambda x: [x[1], -x[0]])
        
        nums = [key for key, val in nums]
        
        return nums
        