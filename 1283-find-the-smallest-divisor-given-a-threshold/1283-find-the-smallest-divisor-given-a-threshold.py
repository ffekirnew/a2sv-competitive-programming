class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        
        while lo < hi:
            mid = lo + ( hi - lo ) // 2
            
            all_sum = sum([ math.ceil(num / mid) for num in nums ])
            
            if all_sum <= threshold:
                prev_sum = sum([ math.ceil(num / mid - 1) for num in nums ]) if mid > 0 else threshold + 1
                if prev_sum > threshold:
                    return mid
                else:
                    hi = mid
            else:
                lo = mid + 1
        
        return lo
                
                
        