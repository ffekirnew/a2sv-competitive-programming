import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # create the object to store the sums in and use for comparing
        queue = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        heapq.heapify(queue)
        
        answer = []
        while queue:
            _, num1_col, num2_col = heapq.heappop(queue)
            answer.append([nums1[num1_col], nums2[num2_col]])
            k -= 1
            
            if not k:
                break
            
            num2_col += 1
            
            if num2_col == len(nums2):
                continue
            
            heapq.heappush(queue, (nums1[num1_col] + nums2[num2_col], num1_col, num2_col))
        
        return answer