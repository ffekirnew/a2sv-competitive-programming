class Solution:
    def numSub(self, s: str) -> int:
        count = 0

        def gauss_sum(n):
            return (n * (n + 1)) // 2
        
        curr_bit, curr_length = None, 0
        for index in range(len(s) + 1):
            if index < len(s):
                bit = s[index]
            else:
                bit = '0'
                
            if bit != curr_bit:
                if curr_bit == '1':
                    count += gauss_sum(curr_length)
                curr_length = 0

            curr_bit = bit
            curr_length += 1
        
        return count % (10 ** 9 + 7)