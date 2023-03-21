class Solution:
    def backtrack(self, curr, index):
        if len(curr) >= 2:
            self.answer.add(tuple(curr))

        if index == len(self.nums):
            return
        
        if not curr or (curr and self.nums[index] >= curr[-1]):
            curr.append(self.nums[index])
            self.backtrack(curr, index + 1)
            curr.pop()

        self.backtrack(curr, index + 1)        
        
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.answer = set()
        
        self.backtrack([], 0)
        
        return list(self.answer)
        