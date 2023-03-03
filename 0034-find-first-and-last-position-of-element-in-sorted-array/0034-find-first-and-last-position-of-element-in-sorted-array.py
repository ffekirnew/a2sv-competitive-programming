class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def hiBinarySearch(lo, hi):
            if lo > hi:
                return -1
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return mid if mid == len(nums) - 1 or nums[mid + 1] != target else hiBinarySearch(mid + 1, hi)
                    
            elif nums[mid] > target:
                return hiBinarySearch(lo, mid - 1)
            else:
                return hiBinarySearch(mid + 1, hi) 
        
        def loBinarySearch(lo, hi):
            if lo > hi:
                return -1
            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return mid if mid == 0 or nums[mid - 1] != target else loBinarySearch(lo, mid - 1)
                    
            elif nums[mid] > target:
                return loBinarySearch(lo, mid - 1)
            else:
                return loBinarySearch(mid + 1, hi)
        
        return [ loBinarySearch(0, len(nums) - 1), hiBinarySearch(0, len(nums) - 1) ]
            