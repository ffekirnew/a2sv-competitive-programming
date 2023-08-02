class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutations = []
        nums = [i + 1 for i in range(n)]
        answer = [None]
        
        def backtrack(curr):
            if len(curr) == len(nums):
                permutations.append(curr) 
                if len(permutations) == k:
                    answer[0] = permutations[-1]
                return
            
            if answer[0]:
                return

            for num in nums:
                if num not in curr:
                    backtrack(curr + [num])
        
        backtrack([])
        return "".join(str(num) for num in answer[0])
        