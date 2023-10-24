class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def str_representation(nums: List[int]) -> str:
            return "".join(map(str, nums))

        nums.sort()

        result = {}
        for index in range(len(nums) - 2):            
            left, right = index + 1, len(nums) - 1
            while left < right:
                triplet = [nums[left], nums[right], nums[index]]
                sum_ = sum(triplet)

                if sum_ == 0:
                    result[str_representation(triplet)] = triplet
                    right -= 1
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    left += 1
        
        return result.values()
                    
                
        