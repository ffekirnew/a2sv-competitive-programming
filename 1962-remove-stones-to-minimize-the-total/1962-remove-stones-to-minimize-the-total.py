import heapq as heap

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # have the piles in a max-heap
        piles = list(map(lambda x: -x, piles))
        heap.heapify(piles)
        
        # for the amount of k, execute the operation
        while k:
            number = heap.heappop(piles)
            number += -1 * number // 2
            heap.heappush(piles, number)
            
            k -= 1
        
        
        # make the elements in the piles positive again
        piles = list(map(lambda x: -x, piles))
        
        # return the sum
        return sum(piles)
        
        
        