class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            while b:
                temp = b
                b = a % b
                a = temp
            
            return a
        
        lcm = lambda x, y: (x * y) / gcd(x, y)
        
        count = 0
        
        for i in range(len(nums)):
            arr_lcm = nums[i]
            
            for j in range(i, len(nums)):
                arr_lcm = lcm(arr_lcm, nums[j])
                
                if arr_lcm > k:
                    break
            
                if arr_lcm == k:
                    count += 1
        
        return count
        