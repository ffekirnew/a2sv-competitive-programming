class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] = [-1 * arr[i], i]
            
        heapify(arr)
        
        answer = []
        for i in range(len(arr) - 1):
            while arr and arr[0][1] <= i:
                heappop(arr)
            answer.append(-1 * arr[0][0])
        
        answer.append(-1)
        
        return answer
            
        