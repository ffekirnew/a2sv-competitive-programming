class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # create obj to be returned
        good_arrays = 0
        nums.append('a')

        # find all unique values
        l, r = 0, 0
        curr = defaultdict(int)
        
        next_unique = {}
        flag = True
        
        while r < len(nums):
            if flag:
                curr[nums[r]] += 1
            
            if len(curr) > k and l < len(nums):
                curr[nums[l]] -= 1
                if not curr[nums[l]]:
                    del curr[nums[l]]
                next_unique[l] = r

                l += 1
                flag = False
                continue

            r += 1
            flag = True
        
        while l < r:
            next_unique[l] = r - 1
            l += 1

        # print(next_unique) # do sliding window
        s = 0
        unique = defaultdict(int)
        
        for e in range(len(nums)):
            unique[nums[e]] += 1
            
            while len(unique) == k:
                good_arrays += next_unique[s] - e
                
                if unique[nums[s]] == 1:
                    del unique[nums[s]]
                else:
                    unique[nums[s]] -= 1
                
                s += 1

        # return the solution
        return good_arrays
            
        