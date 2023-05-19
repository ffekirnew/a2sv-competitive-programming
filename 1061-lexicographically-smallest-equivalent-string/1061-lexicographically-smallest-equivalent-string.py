from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.roots = defaultdict(int)
        self.rank = defaultdict(int)
        self.smallest = defaultdict(str)

    def __repr__(self):
        return f"{self.roots}"

    def add_node(self, x):
        if x in self.roots:
            return

        self.roots[x] = x
        self.smallest[x] = x

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
        if x not in self.roots:
            return x
            
        return self.smallest[self._find(x)]

    def union(self, x, y) -> None:
        self.add_node(x)
        self.add_node(y)

        x_root = self._find(x)
        y_root = self._find(y)

        if x_root == y_root:
            return

        x_rank = self.rank[x_root]
        y_rank = self.rank[y_root]

        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

        if x_rank > y_rank:
            self.roots[y_root] = x_root
        else:
            self.roots[x_root] = y_root

        self.smallest[y_root] = min(self.smallest[y_root], self.smallest[x_root])
        self.smallest[x_root] = min(self.smallest[y_root], self.smallest[x_root])


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_find = UnionFind()
        
        for i in range(len(s1)):
            union_find.union(s1[i], s2[i])
        
        answer = []
        for i, char in enumerate(baseStr):
            answer.append(union_find.lexicographically_smallest_connected(char))
        
        return "".join(answer)
        