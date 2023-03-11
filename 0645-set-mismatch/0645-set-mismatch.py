class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        
        answer = [None, None]
        
        for i in range(1, len(nums) + 1):
            if i in freqs and freqs[i] == 2:
                answer[0] = i
            elif i not in freqs:
                answer[1] = i
        
        return answer
        