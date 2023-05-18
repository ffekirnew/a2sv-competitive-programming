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
        self.size[x] = 1

    def _find(self, x) -> int:
        if x != self.roots[x]:
            self.roots[x] = self._find(self.roots[x])

        return self.roots[x]

    def connected(self, x, y) -> bool:
        if x in self.roots and y in self.roots:
            return self._find(x) == self._find(y)
        return False

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
            self.size[x_root] += self.size[y_root]
        else:
            self.roots[x_root] = y_root
            self.size[y_root] += self.size[x_root]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) == 1:
            return True
        # define the union find data structure
        union_find = UnionFind()
        
        # define helper variables and functions
        rows, cols = len(grid), len(grid[0])
        directions = {
            1: {(0, 1), (0, -1)},
            2: {(1, 0), (-1, 0)},
            3: {(1, 0), (0, -1)},
            4: {(1, 0), (0, 1)},
            5: {(-1, 0), (0, -1)},
            6: {(-1, 0), (0, 1)},
        }
        
        def in_bound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        # iterate in the grid and build the union-find tree
        for row in range(rows):
            for col in range(cols):
                for (new_row, new_col) in directions[grid[row][col]]:
                    nx_row, nx_col = row + new_row, col + new_col
                    if in_bound(nx_row, nx_col) and any((nx_row + r, nx_col + c) == (row, col) for r, c in directions[grid[nx_row][nx_col]]):
                        union_find.union((row, col), (nx_row, nx_col))

        return union_find.connected((0, 0), (rows - 1, cols - 1))
                        
                    
        
        
        