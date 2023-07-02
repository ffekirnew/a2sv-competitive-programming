class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = [0]
        net_transfers = [0] * n
        
        # @cache
        def dp(index, requests_achieved):
            if index >= len(requests):
                if all(not net_transfer for net_transfer in net_transfers):
                    max_requests[0] = max(max_requests[0], requests_achieved)
                return
                
            dp(index + 1, requests_achieved)
            net_transfers[requests[index][0]] -= 1
            net_transfers[requests[index][1]] += 1
            dp(index + 1, requests_achieved + 1)
            net_transfers[requests[index][0]] += 1
            net_transfers[requests[index][1]] -= 1
        
        dp(0, 0)
        return max_requests[0]

        