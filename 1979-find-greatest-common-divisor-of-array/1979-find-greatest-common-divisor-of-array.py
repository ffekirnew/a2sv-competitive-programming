class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
    
        return gcd( sorted(nums)[0], sorted(nums)[-1] )
        