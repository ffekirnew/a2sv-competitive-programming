class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # create the object to be returned
        partitioned = []
        
        # loop thorugh nums three times to add all elements to the list
        for num in nums:
            if num < pivot:
                partitioned.append(num)
                
        for num in nums:
            if num == pivot:
                partitioned.append(num)
                
        for num in nums:
            if num > pivot:
                partitioned.append(num)
        
        return partitioned
        