class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s)
        l, c = 0, Counter(s) 
        
        answer = n
        
        for r in range(n):
            c[s[r]] -= 1

            while l < n and 4 * max(c.values()) <= n:
                answer = min(answer, r-l+1)
                c[ s[l] ] += 1 
                l += 1

        return answer
            
        