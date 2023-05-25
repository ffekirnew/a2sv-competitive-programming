class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        
        for i in range(1, len(arr)):
            arr[i] = (arr[i - 1] + 1) if (arr[i] - arr[i - 1] > 1) else arr[i] 
        
        return arr[-1]
                
        
        
            
        