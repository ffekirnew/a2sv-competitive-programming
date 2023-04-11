class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]
        
        def permutation(curr_arr):
            if len(curr_arr) == len(nums):
                answer.append(curr_arr)
                
            
            for i in range(len(nums)):
                if nums[i] not in curr_arr:
                    last_index = len(curr_arr) + 1
                    if last_index and last_index % nums[i] and nums[i] % last_index:
                        continue

                    permutation(curr_arr + [nums[i]])
            
        answer = []
        permutation([])
        
        return len(answer)
                    
        