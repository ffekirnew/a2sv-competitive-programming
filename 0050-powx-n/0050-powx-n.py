class Solution:
    def __init__(self):
        self.memo = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, n * -1)
            
        
        if not n // 2 in self.memo:
            self.memo[ n // 2 ] = self.myPow(x, (n // 2))
        if not (n // 2 + n % 2) in self.memo:
            self.memo[ (n // 2 + n % 2) ] = self.myPow(x, (n // 2 + n % 2))

        return self.memo[ n // 2 ] * self.memo[ n // 2 + n % 2 ]

                
            
            
        