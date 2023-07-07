class Solution:
    @staticmethod
    def maxConsecutiveWithChange(answers, wanted_value, k):
        max_length = 0

        changed = 0
        left = 0
        for right in range(len(answers)):
            changed += answers[right] != wanted_value
            
            while changed > k:
                changed -= answers[left] != wanted_value
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
            
                
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max( self.maxConsecutiveWithChange(answerKey, 'T', k), self.maxConsecutiveWithChange(answerKey, 'F', k) )
        