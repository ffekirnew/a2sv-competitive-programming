class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(1, len(nums), 2):
            nums.insert(i, nums.pop(n))
            n += 1
            if n > len(nums): 
                break
        
        return nums
        