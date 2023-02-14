class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i, j = len(a)-1, len(b)-1

        while i >= 0 or j >= 0 or carry > 0:
            sum = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:
                sum += int(b[j])
                j -= 1

            result = str(sum % 2) + result
            carry = sum // 2

        return result
            