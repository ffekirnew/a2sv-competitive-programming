class Solution:
    def reverseNumber(self, num: int):
        reversed_number = 0
        while num:
            reversed_number = reversed_number * 10 + num % 10
            num //= 10
        return reversed_number
        
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # reverse and add all reversed numbers to the list
        for i in range(len(nums)):
            nums.append(self.reverseNumber(nums[i]))
            
        # change nums to a set
        nums = set(nums)
        
        # return the length of the set
        return len(nums)
        
        