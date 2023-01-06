class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        number_of_ice_creams = 0
        
        # sort costs
        costs.sort()
        
        # iterate through costs and count all that can be bought
        for cost in costs:
            if coins < cost:
                break
            coins -= cost
            number_of_ice_creams += 1
        
        return number_of_ice_creams
        