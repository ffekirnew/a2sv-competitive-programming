class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(starting_index: int, index: int):
            if index == len(s):
                return starting_index == index

            if (starting_index, index) not in memo:
                memo[(starting_index, index)] = False

                for word in wordDict:
                    if word == s[starting_index: index + 1]:
                        memo[(starting_index, index)] |= dp(index + 1, index + 1)

                memo[(starting_index, index)] |= dp(starting_index, index + 1)

            return memo[(starting_index, index)]

        return dp(0, 0)
        