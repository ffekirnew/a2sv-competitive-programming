class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        is_prime = [ True for _ in range(n) ]
        is_prime[0] = is_prime[1] = False
        
        for i in range(n):
            if is_prime[i]:
                j = i * i
                
                while j < n:
                    is_prime[j] = False
                    j += i
        
        answer = 0
        
        for i, num_is_prime in enumerate(is_prime):
            if num_is_prime:
                answer += 1
        
        return answer
        