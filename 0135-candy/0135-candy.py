class Solution:
    def candy(self, ratings: List[int]) -> int:
        def get_rating(index: int) -> int:
            return inf if index in [-1, len(ratings)] else ratings[index]
        
        memo = {}
        def dp(index: int):
            if index not in memo:
                child_candy = 1
                if get_rating(index) > get_rating(index - 1):
                    neighbor_candy = dp(index - 1)
                    if child_candy <= neighbor_candy:
                        child_candy = neighbor_candy + 1

                if get_rating(index) > get_rating(index + 1):
                    neighbor_candy = dp(index + 1)
                    if child_candy <= neighbor_candy:
                        child_candy = neighbor_candy + 1
                
                memo[index] = child_candy
            
            return memo[index]
        
        candies = 0
        for i in range(len(ratings)):
            candies += dp(i)
            
        return candies
            
            
        