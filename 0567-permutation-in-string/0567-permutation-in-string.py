class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count the charachters in s1
        s1_ctr = Counter(s1)
        # create a window with length equal to s1 in s2
        l, r = 0, len(s1)
        s2_ctr = Counter(s2[:r])
        # loop through s2
        while r <= len(s2):
            if s1_ctr == s2_ctr:
                return True
            if r == len(s2):
                break
            s2_ctr[s2[r]] = s2_ctr.get(s2[r], 0) + 1
            s2_ctr[s2[l]] -= 1
            if not s2_ctr[s2[l]]:
                del s2_ctr[s2[l]]
            l += 1
            r += 1
        # return part of the solution
        return False