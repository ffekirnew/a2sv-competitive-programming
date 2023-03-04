class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        
        prefix = [0]
        for num in nums:
            prefix.append( prefix[-1] + num )
        
        queue = deque()
        
        for num in prefix:
            if queue:
                maximum = max( maximum, num - queue[0] )
                while queue and queue[-1] > num:
                    queue.pop()
                queue.append(num)
            else:
                queue.append(num)

        return maximum
        