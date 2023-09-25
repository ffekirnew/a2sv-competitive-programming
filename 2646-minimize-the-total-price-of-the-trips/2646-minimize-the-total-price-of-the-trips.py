from collections import defaultdict


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # count usages
        tree = defaultdict(list)
        for node_1, node_2 in edges:
            tree[node_1].append(node_2)
            tree[node_2].append(node_1)

        node_freq_in_trips = [0] * n
        def count_node_freq_in_trip(node: int, parent: int, trip_end: int) -> None:
            if node == trip_end:
                node_freq_in_trips[trip_end] += 1
                return True

            for child in tree[node]:
                if child == parent: continue
                if count_node_freq_in_trip(child, node, trip_end):
                    node_freq_in_trips[node] += 1
                    return True      
        
        for start, end in trips:
            count_node_freq_in_trip(start, -1, end)
        
        @cache
        def dp(node: int, parent: int) -> int:
            node_best_solution = {
                "halved": (price[node] // 2) * node_freq_in_trips[node],
                "full": price[node] * node_freq_in_trips[node],
            }
            
            for child in tree[node]:
                if child == parent: continue

                halved, full = dp(child, node)
                
                node_best_solution["full"] += min(halved, full)
                node_best_solution["halved"] += full
            
            return node_best_solution["halved"], node_best_solution["full"]

        return min(dp(0, -1))
            
                
            
        
        