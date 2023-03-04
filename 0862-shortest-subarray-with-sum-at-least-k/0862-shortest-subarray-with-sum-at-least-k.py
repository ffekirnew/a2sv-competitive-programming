class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        answer = float('inf')
        
        prefix = [0]
        for num in nums:
            prefix.append( prefix[-1] + num )
        
        queue = deque()
        
        for i, num in enumerate(prefix):
            while queue and num - prefix[queue[0]] >= k:
                answer = min( answer,  i - queue[0] )
                queue.popleft()

            if not queue or prefix[queue[0]] > num:
                queue.appendleft(i)
            else:
                while prefix[ queue[-1] ] > num:
                    queue.pop()
                queue.append(i)
        
        return answer if answer != float('inf') else -1
                
        