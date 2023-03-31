class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysItTakes(min_weight):
            days_taken = 1
            total_weight = 0

            for weight in weights:
                if total_weight + weight > min_weight:
                    days_taken += 1
                    total_weight = 0

                total_weight += weight

            return days_taken
            
        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = lo + ( hi - lo ) // 2
            
            
            if daysItTakes(mid) > days:
                lo = mid + 1

            else:
                if daysItTakes(mid - 1) > days:
                    return mid
                hi = mid - 1
        
        return lo
            
        