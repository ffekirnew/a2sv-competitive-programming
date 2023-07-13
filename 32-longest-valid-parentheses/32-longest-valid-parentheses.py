class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        longest_ending_at = [0] * len(s)

        for index, char in enumerate(s):
            if char == '(' or index == 0:
                continue

            if s[index - 1] == '(': # we are making a simple valid parenthesis where the ( is right before )
                longest_ending_at[index] = 2

                # Try to combine it with a previous subs
                if index - 1 > 0:
                    longest_ending_at[index] += longest_ending_at[index - 2]

                continue

            # Get the length of the subs ending at right before the index
            prev_subs_length = longest_ending_at[index - 1]

            # we are trying to sandwich it, so find the opening match
            index_of_match = index - prev_subs_length - 1
            if index_of_match >= 0 and s[index_of_match] == '(':
                longest_ending_at[index] = longest_ending_at[index - 1] + 2

                # if we succeedes in making the sandwich, try and combine it with another subs before
                if index_of_match > 0:
                    longest_ending_at[index] += longest_ending_at[index_of_match - 1]
        
        return max(longest_ending_at)
        