class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        
        lo = 0
        hi = citations[-1]
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            pos = bisect_left(citations, mid)
            
            if n - pos >= mid:
                next_pos = bisect_left(citations, mid + 1)
                if n - next_pos < mid + 1:
                    return mid
                
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
        