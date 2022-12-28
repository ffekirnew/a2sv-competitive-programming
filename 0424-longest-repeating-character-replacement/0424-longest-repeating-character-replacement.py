class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create the object to be returned
        max_length = 0
        
        # create a dictionary to keep count of each charachter in the window
        window_freq = defaultdict(int)
        
        # set up the sliding window
        left, right  = 0, 0
        most_frequent_char = 0
        
        # interate the string
        while right < len(s):
            window_freq[s[right]] += 1
            most_frequent_char = max(most_frequent_char, window_freq[s[right]])
            if most_frequent_char + k < (right - left + 1):
                window_freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        
        # return the solution
        return max_length
        