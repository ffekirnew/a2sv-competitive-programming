class Solution:
    def backtrack(self, nums, k_remains, comb, combs, i):
        if not k_remains:
            combs.append(comb.copy())
            return
        if i == len(nums):
            return
        
        comb.append(nums[i])
        self.backtrack(nums, k_remains - 1, comb, combs, i + 1)
        comb.pop()
        self.backtrack(nums, k_remains, comb, combs, i + 1)
        
        

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n + 1)]
        # create the object to be returned
        answer = []
        # call the backtrack
        self.backtrack(nums, k, [], answer, 0)
        # return the solution
        return answer