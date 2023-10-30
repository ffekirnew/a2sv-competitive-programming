class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        S_LENGTH = len(s)
        WORD_LENGTH = len(words[0])
        WINDOW_LENGTH = len(words) * WORD_LENGTH
        results = []

        words_count = defaultdict(int)
        words_char_count = defaultdict(int)
        for word in words:
            words_count[word] += 1
            for char in word:
                words_char_count[char] += 1
        
        left = 0
        window_char_count = defaultdict(int)
        for right in range(S_LENGTH):
            window_char_count[s[right]] += 1
            if right - left + 1 > WINDOW_LENGTH:
                window_char_count[s[left]] -= 1
                if window_char_count[s[left]] == 0:
                    del window_char_count[s[left]]
                left += 1
            
            if window_char_count == words_char_count:
                window_words_count = defaultdict(int)
                for i in range(left, right + 1, WORD_LENGTH):
                    curr_word = s[i:i+WORD_LENGTH]
                    if curr_word not in words_count:
                        break
                    window_words_count[curr_word] += 1
                
                if words_count == window_words_count:
                    results.append(left)
        
        return results
        
        
        