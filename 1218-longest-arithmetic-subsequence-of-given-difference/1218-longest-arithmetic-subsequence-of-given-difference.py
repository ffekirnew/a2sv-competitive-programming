from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int) # going to store element : longest_arithmetic_subsequence
        
        for num in arr:
            dp[num] = dp[num - difference] + 1
        
        return max(list(dp.values()))
        