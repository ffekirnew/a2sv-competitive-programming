class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # brute force
        # answer = 0
        # for i in range(len(nums)):
        #     freq = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] % 2 != 0:
        #             freq += 1
        #         if freq >= k:
        #             answer += 1
        # return answer
        
        # create the solution to be returned
        answer = 0
        # find also the prefix sums using a hahmap
        total = 0
        i = 0
        prefix = {0:1}
        while i < len(nums):
            total += nums[i] % 2
            if total - k in prefix:
                answer += prefix[total - k]
            prefix[total] = prefix.get(total, 0) + 1
            i += 1
        # return the solution
        return answer