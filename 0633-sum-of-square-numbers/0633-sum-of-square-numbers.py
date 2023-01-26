class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)
        
        while left <= right:
            print(left, right)
            if c == left ** 2 + right ** 2:
                return True
            elif c > left ** 2 + right ** 2:
                left += 1
            else:
                right -= 1
        return False
        