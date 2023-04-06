class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        no_incoming = set([ _ for _ in range(n) ])
        
        for edge in edges:
            if edge[1] in no_incoming:
                no_incoming.remove(edge[1])
        
        return list(no_incoming)
