import heapq
from collections import defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ending_at = defaultdict(list)
        
        for num in nums:
            if not ending_at[num - 1]:
                heapq.heappush(ending_at[num], 1)
                
            else:
                min_length_ending_at_last_index = heappop(ending_at[num - 1])
                heapq.heappush(ending_at[num], min_length_ending_at_last_index+1)
                
                
        for val in ending_at.values():
            if val and heapq.heappop(val) < 3:
                return False
            
        return True