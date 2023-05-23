from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.roots = {}
        self.rank = {}
        self.smallest = {}

    def __repr__(self):
        return f"{self.roots}"

    def add_node(self, idx, char):
        if idx in self.roots:
            return
        
        self.roots[idx] = idx
        self.rank[idx] = 0
        self.smallest[idx] = [char]

    def _find(self, x) -> int:
        path = []
        while x != self.roots[x]:
            path.append(x)
            x = self.roots[x]

        # Path compression
        for node in path:
            self.roots[node] = x

        return x

    def connected(self, x, y) -> bool:
        return self._find(x) == self._find(y)
    
    def lexicographically_smallest_connected(self, x):
        return self.smallest[self._find(x)]

    def union(self, x, y) -> None:
        x_root = self._find(x)
        y_root = self._find(y)

        if x_root == y_root:
            return

        x_rank = self.rank[x_root]
        y_rank = self.rank[y_root]

        if x_rank == y_rank:
            self.rank[x_root] += 1
            x_rank += 1

        if x_rank > y_rank:
            self.roots[y_root] = x_root
            while self.smallest[y_root]:
                heapq.heappush(self.smallest[x_root], self.smallest[y_root].pop())
        else:
            self.roots[x_root] = y_root
            while self.smallest[x_root]:
                heapq.heappush(self.smallest[y_root], self.smallest[x_root].pop())

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        letters = UnionFind()
        
        for idx1, idx2 in pairs:
            letters.add_node(idx1, s[idx1])
            letters.add_node(idx2, s[idx2])
            letters.union(idx1, idx2)

        answer = []
        for i, char in enumerate(s):
            letters.add_node(i, char)
            answer.append(heapq.heappop(letters.lexicographically_smallest_connected(i)))
        
        return "".join(answer)
        