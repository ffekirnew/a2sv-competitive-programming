class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def top_sort(indegree: List[int], graph: List[List[int]]) -> int:
            in_degree = indegree.copy()
            queue = [node for node in range(len(in_degree)) if in_degree[node] == 0]
            order = []
            
            while queue:
                node = queue.pop()
                order.append(node)
                
                for child in graph[node]:
                    in_degree[child] -= 1
                    
                    if not in_degree[child]:
                        queue.append(child)
            
            return order

        # If an item belongs to zero group, assign it a unique group id.
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        # Sort all item regardless of group dependencies.
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        
        # Sort all groups regardless of item dependencies.
        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id  
        
        for item in range(n):
            for prev_item in beforeItems[item]:
                item_graph[prev_item].append(item)
                item_indegree[item] += 1
                
                if group[item] != group[prev_item]:
                    group_graph[group[prev_item]].append(group[item])
                    group_indegree[group[item]] += 1

        group_order = top_sort(group_indegree, group_graph)
        item_order = top_sort(item_indegree, item_graph)
        
        if len(group_order) != group_id or len(item_order) != n:
            return []
        
        groups = [[] for _ in range(group_id)]
        queue = [node for node in range(n) if item_indegree[node] == 0]

        while queue:
            node = queue.pop()
            groups[group[node]].append(node)

            for child in item_graph[node]:
                item_indegree[child] -= 1

                if not item_indegree[child]:
                    queue.append(child)

        final_order = []
        for group_index in group_order:
            final_order += groups[group_index]
        
        return final_order