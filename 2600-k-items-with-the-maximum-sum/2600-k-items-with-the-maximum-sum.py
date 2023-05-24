class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k

        sum_ = 0
        while k:
            if numOnes:
                sum_ += 1
                numOnes -= 1
            elif numZeros:
                numZeros -= 1
            elif numNegOnes:
                sum_ -= 1
                numNegOnes -= 1
            
            k -= 1
        
        return sum_
            
                
        