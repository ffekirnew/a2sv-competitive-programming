class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        min_ = -inf
        
        for house in houses:
            right = bisect_left( heaters, house )
            left = right - 1
            
            radius = min( house - (heaters[left] if left > -1 else -inf), (heaters[right] if 0 <= right < len(heaters) else inf) - house )
            min_ = max( min_, radius )
        
        return min_