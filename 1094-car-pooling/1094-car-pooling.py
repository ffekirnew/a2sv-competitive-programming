class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start, end = trips[0][1], trips[0][2]
        for trip in trips:
            start = min( start, trip[1] )
            end = max( end, trip[2] )
        
        prefix_array = [0] * (end - start + 2)
        
        for trip in trips:
            prefix_array[ trip[1] - start ] += trip[0]
            prefix_array[ trip[2] - start ] -= trip[0]
        
        for i in range(len(prefix_array) - 1):
            prefix_array[i] += prefix_array[i - 1] if i > 0 else 0
            if prefix_array[i] > capacity:
                return False
        
        return True