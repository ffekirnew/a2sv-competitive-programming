class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer = []
        for i, num in enumerate(nums):
            if num == target:
                answer.append(i)
        return answer
        