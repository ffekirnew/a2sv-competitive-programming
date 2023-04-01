class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(right + 1):
            
            if is_prime[i]:
                j = i * i

                while j <= right:
                    is_prime[j] = False
                    j += i
            
        
        prev_prime = None
        closest_gap = inf
        answer = [-1, -1]
        
        for i in range(left, right + 1):
            if is_prime[i]:
                if prev_prime and i - prev_prime < closest_gap:
                    closest_gap = i - prev_prime

                    if closest_gap == 1:
                        return [prev_prime, i]

                    answer = [prev_prime, i]
                prev_prime = i
            
        return answer
                        
                    
        