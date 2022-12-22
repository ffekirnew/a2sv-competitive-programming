class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = 0
        i, j, k = n - 3, n - 2, n - 1
        print(nums[i], nums[j], nums[k])
        while i >= 0:
            if nums[i] + nums[j] <= nums[k]:
                i, j, k = i - 1, j - 1, k - 1
            else:
                answer = max(answer, nums[i] + nums[j] + nums[k])
                break
        return answer
        