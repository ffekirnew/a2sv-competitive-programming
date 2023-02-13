class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        
        n = len(nums)
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sums.append(curr)
        
        sums.sort()
        
        answer = 0
        for i in range(left - 1, right):
            answer += sums[i]
        
        return answer % (10 ** 9 + 7)