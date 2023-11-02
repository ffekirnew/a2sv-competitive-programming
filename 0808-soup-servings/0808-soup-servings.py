class OptimizeSoupServings:
    def solve(self, n):
        servings = [ [100, 0], [75, 25], [50, 50], [25, 75] ]

        memo = {}
        def dp(a, b):
            if a <= 0 or b <= 0:
                return a <= 0 and b > 0, a <= 0 and b <= 0, a > 0 and b <= 0
            
            if (a, b) not in memo:
                memo[(a, b)] = [0, 0, 0]
                for serving in servings:
                    a_empty_first, a_and_b_equally_empty, b_empty_first = dp(a - serving[0], b - serving[1])
                    memo[(a, b)][0] += .25 * a_empty_first
                    memo[(a, b)][1] += .25 * a_and_b_equally_empty
                    memo[(a, b)][2] += .25 * b_empty_first

            return memo[(a, b)]
        
        if n > 5000:
            return 1.00000

        result = dp(n, n)
        return (result[0] + result[1] / 2) / sum(result)

class Solution:
    def soupServings(self, n: int) -> float:
        solution = OptimizeSoupServings()
        return solution.solve(n)
                    
                    
        