class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # sanity check
        if len(arr) < 3:
            return False
        
        # check if the arr has started falling right away
        if arr[1] <= arr[0]:
            return False
        
        # create a variable to know if the mountain is increasing or not
        increasing = True
        
        for i in range(2, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            
            elif arr[i] < arr[i - 1]:
                increasing = False
            elif not increasing and arr[i] > arr[i - 1]:
                return False
        
        return not increasing
        