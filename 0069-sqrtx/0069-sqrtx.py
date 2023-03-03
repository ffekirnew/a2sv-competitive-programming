class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x
        
        while lo <= hi:
            mid = (hi + lo) // 2
            
            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid
        
        return lo - 1
        