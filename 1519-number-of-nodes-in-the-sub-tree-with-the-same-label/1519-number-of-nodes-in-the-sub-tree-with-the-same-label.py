class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        
        english_letters = [0] * 26
        
        visited = set()
        def dfs(node):
            visited.add(node)
            
            childs = []
            for child in tree[node]:
                if child not in visited:
                    childs.append(dfs(child))
                    
            alphabet = english_letters.copy()
            for child_alphabet in childs:
                for i in range(26):
                    alphabet[i] += child_alphabet[i]
            
            alphabet[ord(labels[node]) - 97] += 1
            tree[node].append(alphabet[ord(labels[node]) - 97])
            
            return alphabet
        
        dfs(0)
        
        answer = []
        for i in range(len(tree)):
            answer.append(tree[i][-1])
        
        return answer