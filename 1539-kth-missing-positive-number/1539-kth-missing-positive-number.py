class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        integers = { num : 0 for num in range(1, 10000) }
        for num in arr:
            integers[num] += 1
        
        i = 1
        while k:
            if not integers[i]:
                k -= 1
            
            if k == 0:
                return i
            
            i += 1
            
            
        