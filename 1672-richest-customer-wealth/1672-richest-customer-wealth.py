class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_wealth = 0
        
        for customer in accounts:
            max_wealth = max(sum(customer), max_wealth)
            
        return max_wealth
        