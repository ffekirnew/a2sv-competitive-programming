from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        time_taken = [0 for _ in range(n)]
        has_dependency = [0 for _ in range(n)]
        dependent_jobs = defaultdict(list)

        for dep, job in edges:
            dependent_jobs[dep].append(job)
            has_dependency[job - 1] += 1
            
        queue = [job for job in range(1, n + 1) if not has_dependency[job - 1]]
        time = 0

        while queue:
            new_queue = []
            
            for job in queue:
                time_taken[job - 1] = time + 1
            
                for dependent_job in dependent_jobs[job]:
                    has_dependency[dependent_job - 1] -= 1
                    
                    if has_dependency[dependent_job - 1] == 0:
                        new_queue.append(dependent_job)
            
            queue = new_queue
            time += 1
        
        return time_taken

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends