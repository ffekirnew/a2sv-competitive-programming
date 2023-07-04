class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first_time, second_time, thrid_time = 0, 0, 0
        
        for num in nums:
            second_time |= first_time & num
            first_time ^= num
            thrid_time = first_time & second_time
            
            first_time &= ~thrid_time
            second_time &= ~thrid_time
        
        return first_time
            
        