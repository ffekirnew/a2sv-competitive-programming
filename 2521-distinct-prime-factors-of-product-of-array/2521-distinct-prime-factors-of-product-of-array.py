class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factorization(num: int):
            d = 2
            factorization = set()
            
            while d * d <= num:
                while num % d == 0:
                    factorization.add(d)
                    num //= d
                d += 1
            
            if num != 1:
                factorization.add(num)
            
            return factorization
        
        all_factors = set()
        for num in nums:
            all_factors = all_factors.union(prime_factorization(num))
            
        
        return len(all_factors)
        