class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        sorted_ = []
        
        for num in nums:
            heappush(heap, num)
        
        while heap:
            sorted_.append(heappop(heap))
        
        return sorted_
        