class Solution:
    def nextSmaller(self, arr: List[int]) -> int:
        n = len(arr)
        next_smaller = [0] * len(arr)

        stack = []        
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            
            next_smaller[i] = stack[-1][1] if stack else n
            stack.append( [ arr[i], i ] )

        return next_smaller
    
    def prevSmaller(self, arr: List[int]) -> int:
        n = len(arr)
        prev_smaller = [0] * len(arr)
        
        stack = []        
        for i in range(n):
            while stack and stack[-1][0] > arr[i]:
                stack.pop()
            
            prev_smaller[i] = stack[-1][1] if stack else -1
            stack.append( [ arr[i], i ] )
        
        return prev_smaller

    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_of_subarray_mins = 0
        
        prev_smaller = self.prevSmaller(arr)
        next_smaller = self.nextSmaller(arr)
        
        for i, num in enumerate(arr):
            sum_of_subarray_mins += num * (i - prev_smaller[i]) * (next_smaller[i] - i)
        
        return sum_of_subarray_mins % (10 ** 9 + 7)
        
        
            