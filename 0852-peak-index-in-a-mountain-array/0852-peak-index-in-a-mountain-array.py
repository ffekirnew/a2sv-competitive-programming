class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        
        while True:
            mid = lo + ( hi - lo ) // 2
            
            if 0 < mid < len(arr) - 1 and arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        