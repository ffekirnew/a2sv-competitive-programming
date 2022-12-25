class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # create the object to be returned
        answer = []
        # sort nums since subsequence is what is required
        nums.sort()
        # set up a sliding window and run through nums
        for query in queries:
            left, right = 0, 0
            curr = 0
            max_length = 0
            while right < len(nums):
                curr += nums[right]
                while curr > query:
                    curr -= nums[left]
                    left += 1
                right += 1
                max_length = max(right - left, max_length)
            answer.append(max_length)
        # return the solution
        return answer