class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def str_rep(nums: List[int]) -> str:
            return "".join(list(map(str, nums)))

        results = {}

        nums.sort()
        
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                new_target = target - (nums[i] + nums[j])
                
                left, right =  j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == new_target:
                        quadruplet = [nums[i], nums[j], nums[left], nums[right]]
                        results[str_rep(quadruplet)] = quadruplet
                        
                    if nums[left] + nums[right] < new_target:
                        left += 1
                    else:
                        right -= 1
        
        return list(results.values())
                
        