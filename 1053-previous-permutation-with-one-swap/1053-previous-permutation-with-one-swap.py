class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i >= 0:
            max_greater_idx = i + 1
            # Find the maximum number greater than A[i] on the right that is less than A[i]
            for j in range(max_greater_idx + 1, len(arr)):
                if arr[max_greater_idx] < arr[j] < arr[i]:
                    max_greater_idx = j
            # Swap the two elements to get the previous permutation
            arr[max_greater_idx], arr[i] = arr[i], arr[max_greater_idx]
        return arr

        