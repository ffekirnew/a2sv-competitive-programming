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
    
    def cantors_diagonal(self):
        answer = []
        
        for i, num in enumerate(nums):
            answer.append("1" if num[i] == "0" else "0")
        
        return "".join(answer)

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        solution = FindUniqueBinaryString(nums)
        return solution.approach_1()
        
        