class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counting_sort = [0] * len(nums)
        
        for num in nums:
            counting_sort[num - 1] += 1
        
        answer = []
        for i, num in enumerate(counting_sort):
            if num == 2:
                answer.append(i + 1)
        
        return answer
        