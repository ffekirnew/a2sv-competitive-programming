class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, x) -> int:
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x, y) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return
        x_rank, y_rank = self.rank[x_root], self.rank[y_root]
        
        if self.rank[x_root] == self.rank[y_root]: self.rank[x_root] += 1

        if x_rank > y_rank: self.roots[y_root] = x_root
        else: self.roots[x_root] = y_root


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        
        for from_, to_ in edges:
            if union_find.connected(from_ - 1, to_ - 1):
                return [from_, to_]
            
            union_find.union(from_ - 1, to_ - 1)
        
        return
        