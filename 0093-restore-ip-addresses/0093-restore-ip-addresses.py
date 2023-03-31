class Solution:
    def backtrack(self, curr, index, left_segments):
        if index == len(self.s):
            if not left_segments:
                self.addresses.append(".".join(curr))
            return
        
        self.backtrack(curr + [self.s[index]], index + 1, left_segments - 1)
        if curr and curr[-1] != '0' and int(curr[-1] + self.s[index]) <= 255:
            curr[-1] += self.s[index]
            self.backtrack(curr, index + 1, left_segments)
            
        
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.addresses = []
        
        # do something
        self.backtrack([], 0, 4)
        
        return self.addresses
        