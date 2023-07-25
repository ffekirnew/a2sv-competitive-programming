class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visit = [False] * n
        indegree = [0] * n

        # Count indegree of each node.
        for edge in edges:
            if edge != -1:
                indegree[edge] += 1

        # Kahn's algorithm starts.
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            visit[node] = True
            neighbor = edges[node]
            if neighbor != -1:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        # Kahn's algorithm ends.

        answer = -1
        for i in range(n):
            if not visit[i]:
                neighbor = edges[i]
                count = 1
                visit[i] = True
                # Iterate in the cycle.
                while neighbor != i:
                    visit[neighbor] = True
                    count += 1
                    neighbor = edges[neighbor]
                answer = max(answer, count)
        return answer
