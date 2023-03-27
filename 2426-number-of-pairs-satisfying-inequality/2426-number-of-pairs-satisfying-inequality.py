class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        answer = [0]
        nums = [ nums1[i] - nums2[i] for i in range(len(nums1)) ]
        
        def merge(l1, l2):
            merged = []
            i, j = 0, 0
            
            l1.append(inf)
            l2.append(inf)
            
            while i < len(l1) and j < len(l2):
                if l1[i] <= l2[j]:
                    merged.append(l1[i])
                    i += 1
                else:
                    merged.append(l2[j])
                    j += 1
            
            merged.pop()
            return merged
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left_sorted, right_sorted = merge_sort(nums[:mid]), merge_sort(nums[mid:])
            
            j = 0
            for i in range(len(left_sorted)):
                while j < len(right_sorted):
                    if left_sorted[i] <= right_sorted[j] + diff:
                        answer[0] += len(right_sorted) - j
                        break
                    else:
                        j += 1
            
            return merge(left_sorted, right_sorted)
        
        merge_sort(nums)
        
        return answer[0]