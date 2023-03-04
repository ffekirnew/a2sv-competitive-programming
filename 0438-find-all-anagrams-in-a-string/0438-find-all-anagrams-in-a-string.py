class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # create the object to be returned
        answer = []
        # count s and p
        k = len(p)
        p = Counter(p)
        # set up the sliding window
        curr = Counter(s[:k])
        if curr == p:
            answer.append(0)
        for i in range(1, len(s) - k + 1):
            curr[s[i+k-1]] = curr.get(s[i+k-1], 0) + 1
            if curr[s[i - 1]] > 1:
                curr[s[i - 1]] -= 1
            else:
                del curr[s[i - 1]]
            if curr == p:
                answer.append(i)
        # return the solution
        return answer
        