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
        x_root = self.find(x)
        y_root = self.find(y)

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

        return


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        
        union_find = UnionFind(rows)
        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c]:
                    union_find.union(r, c)
        
        provinces_seen = set()
        
        # do something
        for r in range(rows):
            provinces_seen.add(union_find.find(r))
        
        return len(provinces_seen)
                    
        