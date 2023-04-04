class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        
        is_prime = [ True ] * 1001
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, len(is_prime)):
            if is_prime[i]:
                j = i * i
                
                while j < len(is_prime):
                    is_prime[j] = False
                    
                    j += i
        
        def solve(n: int):
            if is_prime[n]:
                return n
                    
            biggest_divisor = None

            for i in range(1, n):
                if n % i == 0:
                    biggest_divisor = i

            return (n // biggest_divisor) + solve(biggest_divisor)
        
        
        return solve(n)
        
        