class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if not b:
                return a
            return gcd(b, a % b)
        
        count = 0
        
        for i in range(len(nums)):
            arr_gcd = nums[i]
            
            for j in range(i, len(nums)):
                arr_gcd = gcd(arr_gcd, nums[j])
                
                if arr_gcd < k:
                    break
            
                if arr_gcd == k:
                    count += 1
        
        return count
        