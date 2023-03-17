class Solution:
    def backtrack(self, num1, num2, index):
        if index == len(self.num):
            return True
        for k in range(index + 1, len(self.num) + 1):
            curr_num = int(self.num[index:k])
            
            if len(str(curr_num)) == (k - index) and curr_num == num1 + num2:
                if self.backtrack(num2, curr_num, k):
                    return True
        return False
            
    def isAdditiveNumber(self, num: str) -> bool:
        self.num = num
        for i in range(1, len(num)):
            num1 = int(num[:i])
            
            if not len(str(num1)) == i:
                continue

            for j in range(i + 1, len(num)):
                num2 = int(num[i:j])
                
                if len(str(num2)) == (j - i) and self.backtrack(num1, num2, j):
                    return True
        return False
        
        