class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        arr,n = [0] + arr, len(arr) + 1

        ans, queue  = [0] * n, deque([0])

        for i in range(n):
            while arr[queue[0]] > arr[i]:
                queue.popleft()
            ans[i] = ans[queue[0]] + (i-queue[0]) * arr[i]
            queue.appendleft(i)

        return sum(ans) % (10 ** 9 + 7)