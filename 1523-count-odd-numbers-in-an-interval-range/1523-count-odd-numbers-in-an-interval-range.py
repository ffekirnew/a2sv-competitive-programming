class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low + 1
        
        if (diff % 2):
            if high % 2:
                return math.ceil(diff / 2)
            else:
                return math.floor(diff / 2)
        else:
            return diff // 2
        