class Solution:    
    def countSmaller(self, nums: List[int], root: bool = True) -> List[int]:
        answer = [0] * len(nums)
        nums = [ [num, i] for i, num in enumerate(nums) ]
        
        def merge(l1, l2):
            merged = []
            i, j = 0, 0
            
            l1.append([inf, 0])
            l2.append([inf, 0])
            
            while i < len(l1) and j < len(l2):
                if l1[i][0] <= l2[j][0]:
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
            
            j = len(right_sorted) - 1
            for i in range(len(left_sorted) - 1, -1, -1):
                while j >= 0:
                    if left_sorted[i][0] > right_sorted[j][0]:
                        answer[left_sorted[i][1]] += j + 1
                        break
                    else:
                        j -= 1
            
            return merge(left_sorted, right_sorted)
        
        merge_sort(nums)
        
        return answer
        