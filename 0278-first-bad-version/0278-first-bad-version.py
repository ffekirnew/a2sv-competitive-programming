# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        while lo < n:
            mid = (n + lo) // 2
            
            if isBadVersion(mid):
                n = mid
            else:
                lo = mid + 1
        
        return lo