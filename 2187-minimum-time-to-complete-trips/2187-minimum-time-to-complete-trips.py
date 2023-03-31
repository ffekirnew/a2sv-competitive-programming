class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        
        lo = min(time)
        hi = totalTrips * max(time)
        
        while lo < hi:
            mid = lo + ( hi - lo ) // 2
            
            curr_trips = sum( mid // trip_time for trip_time in time)
            
            if curr_trips >= totalTrips:
                prev_trips = sum( (mid - 1) / trip_time for trip_time in time)
                if prev_trips < totalTrips:
                    return mid
                
                hi = mid
            
            else:
                lo = mid + 1
        
        return lo
        