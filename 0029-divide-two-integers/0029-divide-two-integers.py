class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_LIMIT, MAX_LIMIT = -(2 ** 31), 2 ** 31 - 1
        is_negative = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        remainder = 0

        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                quotient |= (1 << i)
                dividend -= (divisor << i)
                
        

        return max(MIN_LIMIT, min(MAX_LIMIT, is_negative * quotient))