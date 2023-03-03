class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        
        while lo <= hi:
            mid = lo + ( hi - lo ) // 2
            
            total_hours = sum([ math.ceil( pile / mid ) for pile in piles ])
            
            if total_hours == h:
                prev_total_hours = sum([ math.ceil( pile / (mid - 1 )) for pile in piles ]) if mid > 1 else inf
                
                if prev_total_hours != h:
                    return mid
                
                hi = mid - 1
            
            elif total_hours < h:
                hi = mid - 1
            
            else:
                lo = mid + 1

        return lo
            
        