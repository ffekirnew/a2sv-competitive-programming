class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda x: -x, piles))
        
        heapify(piles)
        
        while k:
            number = heappop(piles)
            number += -1 * number // 2
            heappush(piles, number)
            
            k -= 1
        
        
        piles = list(map(lambda x: -x, piles))
        
        return sum(piles)
        
        
        