from collections import defaultdict

sys.setrecursionlimit(100_001)

class UnionFind:
    def __init__(self):
        self.roots = defaultdict(int)
        self.rank = defaultdict(int)
        self.size = defaultdict(int)

    def __repr__(self):
        return f"{self.roots}"

    def add_node(self, x):
        if x in self.roots:
            return

        self.roots[x] = x
        self.rank[x] = 0
        self.size[x] = 1  if type(x) is tuple else 0 # Initialize size to 1 for the new node

    def rank_of(self, x):
        return self.rank[self._find(x)]

    def root_of(self, x):
        return self.roots[self._find(x)]

    def size_of(self, x):
        return self.size[self._find(x)]

    def _find(self, x) -> int:
        if x != self.roots[x]:
            self.roots[x] = self._find(self.roots[x])

        return self.roots[x]

    def connected(self, x, y) -> bool:
        return self._find(x) == self._find(y)

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
            self.size[x_root] += self.size[y_root]  # Update size of the merged set
        else:
            self.roots[x_root] = y_root
            self.size[y_root] += self.size[x_root]  # Update size of the merged set

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        union_find = UnionFind()
        
        for (r, c) in stones:
            union_find.union(f'r{r}', (r, c))
            union_find.union(f'c{c}', (r, c))
        
        answer = 0
        seen = set()
        for key in union_find.roots.keys():
            if union_find.root_of(key) not in seen:
                seen.add(union_find.root_of(key))
                answer += union_find.size_of(key) - 1
        
        return answer
            
        