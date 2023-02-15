class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = 0
        for i in range(len(num)):
            nums = nums * 10 + num[i]
        
        nums += k
        
        result = []
        while nums > 0:
            result.append(nums % 10)
            nums //= 10
        
        return reversed(result)