class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        
        prefix_range = [0] * (len(nums) + 1)
        
        for req in requests:
            prefix_range[req[0]] += 1
            prefix_range[req[1] + 1] -= 1
        
        for i in range(len(prefix_range)):
            prefix_range[i] += prefix_range[i - 1] if i > 0 else 0
        
        prefix_range.pop()     
        
        prefix_range = list(zip(prefix_range, [ i for i in range(len(nums) + 1)]))
        real_nums = [0] * len(nums)
        
        prefix_range.sort(reverse=True, key=lambda x: [x[0], -x[1]])
        
        for i in range(len(nums)):
            real_nums[prefix_range[i][1]] = nums.pop()
        
        for i in range(len(real_nums)):
            real_nums[i] += real_nums[i - 1] if i > 0 else 0
        
        total = 0
        
        for req in requests:
            curr = real_nums[req[1]]
            curr -= real_nums[req[0] - 1] if req[0] > 0 else 0
            total += curr
        
        return total % (10 ** 9 + 7)
        
        
        