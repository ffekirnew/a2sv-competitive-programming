class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # create the object to be returned
        answer = float('inf')
        # set up the sliding window
        s = 0
        e = 0
        curr = 0
        # loop through nums
        while e < len(nums):
            curr += nums[e]
            if curr >= target:
                while curr - nums[s] >= target:
                    curr -= nums[s]
                    s += 1
                answer = min(answer, e - s + 1)
            e += 1
        # return the solution
        return 0 if (answer == float('inf')) else answer
        