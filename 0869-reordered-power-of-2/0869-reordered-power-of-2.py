class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        n = Counter(str(n))
        
        powers_of_2 = []
        
        for i in range(100):
            power = 2 ** i
            if power > 10 ** 9:
                break
            powers_of_2.append([str(power), Counter(str(power))])
        
        for power in powers_of_2:
            if int(power[0]) and power[1] == n:
                return True
        
        return False
        
        
        