from typing import List
from collections import defaultdict

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visited = set()

		def dfs(node, parent):
	        visited.add(node)
	        
		    for child in adj[node]:
		        if child not in visited:
    		        if dfs(child, node):
    		            return True
    		            
		        elif child != parent:
		            return True
		            
    		return False
    	
    	for i in range(len(adj)):
    	    if i not in visited:
    	        if dfs(i, -1):
    	            return True
    	
    	return False
		            


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
