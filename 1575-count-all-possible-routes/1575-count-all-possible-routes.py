class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @cache
        def dp(index, fuel):
            if fuel < 0:
                return 0
            
            count = int(index == finish)
            for i in range(len(locations)):
                if i == index:
                    continue
                
                count += dp(i, fuel - abs(locations[index] - locations[i]))
            
            return count
        
        return dp(start, fuel) % (10 ** 9 + 7)
        