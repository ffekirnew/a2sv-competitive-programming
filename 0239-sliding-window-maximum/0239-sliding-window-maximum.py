import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # create the object to be returned
        max_sliding_window = []
        
        # Initialize the sliding window
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        max_sliding_window.append(-1 * heap[0][0])
        

        # move the sliding window
        left = 0
        for right in range(k, len(nums)):
            heapq.heappush(heap, (-nums[right], right))
            left += 1

            max_element, index = heap[0]
            while not left <= index <= right and heap:
                heapq.heappop(heap)
                max_element, index = heap[0]
            
            if heap:
                max_sliding_window.append(-max_element)

            
        # return the list max list
        return max_sliding_window
        