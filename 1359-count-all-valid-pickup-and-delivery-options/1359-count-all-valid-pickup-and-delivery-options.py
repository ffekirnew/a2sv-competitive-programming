class Solution:
    def countOrders(self, n: int) -> int:
      MOD = 10 ** 9 + 7
      
      memo = {}
      def dp(pickups_left: int, deliveries_left: int) -> int:
        if pickups_left == deliveries_left == 0:
          return 1

        if pickups_left < 0:
          return 0
        
        if (pickups_left, deliveries_left) not in memo:
          ways = pickups_left * dp(pickups_left - 1, deliveries_left)
          if deliveries_left > pickups_left:
            ways += (deliveries_left - pickups_left) * dp(pickups_left, deliveries_left - 1)
          
          memo[(pickups_left, deliveries_left)] = ways % MOD
        
        return memo[(pickups_left, deliveries_left)]
      
      return dp(n, n) % MOD
        