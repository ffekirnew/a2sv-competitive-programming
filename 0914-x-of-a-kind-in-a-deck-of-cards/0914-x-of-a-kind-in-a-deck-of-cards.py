class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        
        
        cards_count = list(Counter(deck).values())
        partition_length = inf
        running_gcd = cards_count[0]
        
        for i in range(len(cards_count)):
            running_gcd = gcd(running_gcd, cards_count[i])
            partition_length = min( partition_length, running_gcd )
        
        return partition_length > 1
        