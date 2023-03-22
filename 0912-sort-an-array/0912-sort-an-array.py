class Solution:
    def merge(self, left, right):
        i, j = 0, 0
        sorted = []
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1
        
        while i < len(left):
            sorted.append(left[i])
            i += 1
        
        while j < len(right):
            sorted.append(right[j])
            j += 1
        
        return sorted
        
        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
        