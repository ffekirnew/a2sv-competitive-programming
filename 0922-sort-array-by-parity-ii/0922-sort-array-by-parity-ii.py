class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = [num for num in nums if not num % 2]
        odds = [num for num in nums if num % 2]
        
        answer = []
        for i in range(len(evens)):
            answer.append(evens[i])
            answer.append(odds[i])
        
        return answer