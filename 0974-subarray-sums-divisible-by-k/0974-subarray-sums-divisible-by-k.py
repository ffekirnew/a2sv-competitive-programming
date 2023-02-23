class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # create the object to be returned
        answer = 0
        # use a freq hashmap to keep track of previous remainders
        prev = {0:1}
        curr = 0
        # loop through nums
        for num in nums:
            curr += num
            div = curr % k
            if (div) in prev:
                answer += prev[div]
            prev[div] = prev.get(div, 0) + 1
        # return the solution
        return answer
        