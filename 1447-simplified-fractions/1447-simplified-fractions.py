class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        answer = []
        factors = set()
        
        for i in range(2, n + 1):
            for j in range(1, i):
                if i / j not in factors:
                    answer.append(f"{j}/{i}")
                    factors.add(i / j)
        
        return sorted(answer)
            
        