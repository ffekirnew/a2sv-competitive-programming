class Solution:
    def rec(self, sums, i):
        if i > len(self.cookies) or len(self.cookies) - i < sums.count(0):
            return
        if i == len(self.cookies):
            curr = -inf
            for bag in sums:
                curr = max(sums)
            self.unfairness[0] = min(curr, self.unfairness[0])
            return

        
        for j in range(len(sums)):
            sums[j] += self.cookies[i]
            self.rec(sums, i + 1)
            sums[j] -= self.cookies[i]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.cookies = cookies
        self.unfairness = [inf]
        
        self.rec([0] * k, 0)
        
        return self.unfairness[0]
        
        