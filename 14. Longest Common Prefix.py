class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        for i in range(len(strs[0])):
            target, found = strs[0][i], True
            for str in strs:
                if str[i] != target:
                    found = False
                    break
            if found:
                ans += target
            else:
                break
        return ans