class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # validate the edge case
        co = len(nums) // 2 - 1 if (len(nums) % 2 == 0) else len(nums) // 2
        if k > co:
            return [-1] * len(nums)
        # create the math formula
        window_len = (k * 2 + 1)
        # create the object to be returned
        # fill answer with -1 untill it gets to the index where we can add i - k and i + k
        answer = [-1] * k
        # create a variable index to travrse the array with
        i = k
        # loop through nums with the rules
        curr = sum(nums[i-k:i+k+1])
        while i < len(nums) - k:
            answer.append(curr // window_len)
            if i + k + 1 < len(nums):
                curr += nums[i + k + 1] - nums[i - k]
            i += 1
        # fill the answer untill the end with -1
        answer += [-1] * k
        # return the solution
        return answer
        