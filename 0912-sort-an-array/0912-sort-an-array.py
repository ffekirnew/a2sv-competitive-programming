class Solution:
    def merge(self, left, right):
        i, j = 0, 0
        sorted_array = []
        
        while i < len(left) or j < len(right):
            if i == len(left):
                sorted_array.append(right[j])
                j += 1

            elif j == len(right):
                sorted_array.append(left[i])
                i += 1

            elif left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        return sorted_array
        
        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
        