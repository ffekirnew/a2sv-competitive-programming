class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create the object to be returned
        answer = 0
        # create a hashmap to keep track of prefix sums
        p = {0 : 1}
        curr = 0
        # loop through the nums
        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in p:
                answer += p[curr - k]
            p[curr] = p.get(curr, 0) + 1
            
        # return the solution
        return answer