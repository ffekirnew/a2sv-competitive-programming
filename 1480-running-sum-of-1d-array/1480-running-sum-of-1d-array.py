class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # create the object to be returned
        answer = []
        # loop through nums and implement prefix sum
        for i in nums:
            if not answer:
                answer.append(i)
            else:
                answer.append(i + answer[-1])
        # return the solution
        return answer