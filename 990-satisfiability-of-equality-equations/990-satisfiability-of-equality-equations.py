from collections import defaultdict

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
        path = []
        while x != self.roots[x]:
            path.append(x)
            x = self.roots[x]

        # Path compression
        for node in path:
            self.roots[node] = x

        return x

    def connected(self, x, y) -> bool:
        if x in self.roots and y in self.roots:
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
            self.size[x_root] += self.size[y_root]
        else:
            self.roots[x_root] = y_root
            self.size[y_root] += self.size[x_root]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = UnionFind()
        
        for equation in equations:
            if "==" in equation:
                var1, var2 = equation.split("==")

                equals.union(var1, var2)
        
        for equation in equations:
            if "!=" in equation:
                var1, var2 = equation.split("!=")

                if var1 == var2 or equals.connected(var1, var2):
                    return False
        
        return True
        
        