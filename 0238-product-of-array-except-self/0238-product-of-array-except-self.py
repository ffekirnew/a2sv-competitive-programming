class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create the object to be returned
        answer = []
        # find prefix and suffix multiples
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in reversed(nums):
            suffix.append(suffix[-1] * num)
        # loop through nums finding the products of all elements except self
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[-(i+2)])
        # return the solution
        return answer
        