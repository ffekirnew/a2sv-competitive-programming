class FindUniqueBinaryString:
    def __init__(self, nums: List[str]):
        self.nums = nums
        self.N = len(nums)
        
    def approach_1(self):
        def pad(num: str):
            return "0" * (self.N - len(num)) + num

        nums_set = set()
        
        for num in self.nums:
            nums_set.add(int(num, 2))
        
        for i in range(pow(2, self.N)):
            if i not in nums_set:
                return pad(bin(i)[2:])
        
        


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        solution = FindUniqueBinaryString(nums)
        return solution.approach_1()
        
        