class LongestHappyPrefix:
    def __init__(self, string: str):
        self.string = string


    def kmp(self):
        self.lps = [0] * len(self.string)
        prev_lps, index = 0, 1

        while index < len(self.string):
            if self.string[prev_lps] == self.string[index]:
                self.lps[index] = prev_lps + 1
                prev_lps += 1
                index += 1
                
            else:
                if prev_lps == 0:
                    index += 1
                else:
                    prev_lps = self.lps[prev_lps - 1]
        
        # print(self.lps)
        length = len(self.string)
        return self.string[length - self.lps[-1]:]



class Solution:
    def longestPrefix(self, s: str) -> str:
        solution = LongestHappyPrefix(s)
        return solution.kmp()
        
        