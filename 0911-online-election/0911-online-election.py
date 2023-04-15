class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.votes = []
        self.count = collections.Counter()
        for p, t in zip(persons, times):
            self.count[p] = c = self.count[p] + 1
            while len(self.votes) <= c: self.votes.append([])
            self.votes[c].append((t, p))

    def q(self, t):
        lo, hi = 1, len(self.votes)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if self.votes[mid][0][0] <= t:
                lo = mid + 1
            else:
                hi = mid
        i = lo - 1
        j = bisect.bisect(self.votes[i], (t, float('inf')))
        return self.votes[i][j-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)