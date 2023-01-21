class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        index = 2
        for i in range(len(piles) // 3):
            piles.insert(index, piles.pop())
            index += 3
            
        result = 0
        for i in range(1, len(piles), 3):
            result += piles[i]
        print(piles)
        return result