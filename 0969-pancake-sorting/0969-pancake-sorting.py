class Solution:
    def __init__(self):
        self.answer = []
    def reverse(self, arr: List[int], idx: int) -> List[int]:
        return list( reversed( arr[ :idx + 1 ] ) ) + arr[ idx + 1: ]

    def pancakeSort(self, arr: List[int]) -> List[int]:

        if len(arr) == 1:
            return self.answer

        # find largest
        idx_largest = 0
        for idx in range(len(arr)):
            idx_largest = idx if arr[idx] > arr[idx_largest] else idx_largest

        # if largest at the end, repeat this process for the remaining list
        if idx_largest != len(arr) - 1:
            arr = self.reverse( arr, idx_largest )
            self.answer.append(idx_largest + 1)
            arr.reverse()
            self.answer.append(len(arr))
            
        return self.pancakeSort( arr[:-1] )
        
        
        