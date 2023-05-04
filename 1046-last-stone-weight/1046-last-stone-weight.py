class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        # change the array to a max-heap
        #-> since there is no max-heap in python, change it to a mean heap after converting each value to a negative
        stones = [-i for i in stones]
        heapify(stones)
        # loop and smash the stones until only 1 element is left
        #-> every time around pop two elements one by one, convert them to positive and compare them
        #-> if they are equal, continue without compensating
        #-> else, continue by adding the difference to the heap
        while len(stones) > 1:
            val1 = -1 * heappop(stones)
            val2 = -1 * heappop(stones)
            if val1 > val2:
                heappush(stones, val2 - val1)
        # return that element
        return 0 if not stones else stones[0] if stones[0] >= 0 else stones[0] * -1
        
        
        