class Solution:
    def numSplits(self, s: str) -> int:
        answer = 0
        
        right_freq = Counter(s)
        left_freq = defaultdict(int)
        
        for char in s:
            left_freq[char] += 1
            right_freq[char] -= 1
            
            if not right_freq[char]:
                del right_freq[char]
                
            if len(right_freq) == len(left_freq):
                answer += 1
        
        return answer
                
        