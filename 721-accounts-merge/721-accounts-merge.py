from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.roots = defaultdict(int)
        self.rank = defaultdict(int)
        self.names = defaultdict(str)

    def __repr__(self):
        return f"{self.roots}"

    def add_node(self, x, name):
        if x in self.roots:
            return

        self.roots[x] = x
        self.rank[x] = 0
        self.names[x] = name
    
    def get_name(self, x):
        if x in self.roots:
            return self.names[self._find(x)]

    def _find(self, x) -> int:
        path = []
        while x != self.roots[x]:
            path.append(x)
            x = self.roots[x]

        for node in path:
            self.roots[node] = x

        return x

    def connected(self, x, y) -> bool:
        if x in self.roots and y in self.roots:
            return self._find(x) == self._find(y)

    def union(self, x, y) -> None:
        x_root = self._find(x)
        y_root = self._find(y)

        if x_root == y_root:
            return

        x_rank = self.rank[x_root]
        y_rank = self.rank[y_root]

        if x_rank < y_rank:
            self.roots[x_root] = y_root
            self.names[y_root] = self.names[x_root]
        elif x_rank > y_rank:
            self.roots[y_root] = x_root
            self.names[x_root] = self.names[y_root]
        else:
            self.roots[y_root] = x_root
            self.names[x_root] = self.names[y_root]
            self.rank[x_root] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts.sort()

        emails = UnionFind()

        for account in accounts:
            name = account[0]
            emails.add_node(account[1], name)
            
            for i in range(2, len(account)):
                emails.add_node(account[i], name)
                emails.union(account[i - 1], account[i])
        
        answer = {}
        
        for account in accounts:
            for i in range(1, len(account)):
                email = account[i]
                
                if emails._find(email) not in answer:
                    answer[emails._find(email)] = [account[0]]
                
                if email not in answer[emails._find(email)]:
                    answer[emails._find(email)].append(email)
        
        real_answer = []
        for account in answer.values():
            name = account.pop(0)
            account.sort()
            
            account.insert(0, name)
            
            real_answer.append(account)
        
        return real_answer
