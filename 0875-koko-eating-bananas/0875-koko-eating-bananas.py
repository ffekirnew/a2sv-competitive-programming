class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        
        while lo <= hi:
            mid = lo + ( hi - lo ) // 2
            
            all_sum = sum([ math.ceil( pile / mid ) for pile in piles ])
            
            if all_sum == h:
                prev_all_sum = sum([ math.ceil( pile / (mid - 1 )) for pile in piles ])
                
                if prev_all_sum != h:
                    return mid
                
                hi = mid
            
            elif all_sum < h:
                hi = mid - 1
            
            else:
                lo = mid + 1

        return lo
            
        