class Solution:
    def minSteps(self, s: str, t: str) -> int:
        answer = 0
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        
        for char in s:
            s_freq[char] += 1
        for char in t:
            t_freq[char] += 1
            
        for char in s_freq.keys():
            if s_freq[char] >= t_freq[char]:
                answer += s_freq[char] - t_freq[char]
            
        for char in t_freq.keys():
            if t_freq[char] >= s_freq[char]:
                answer += t_freq[char] - s_freq[char]
        
        return answer
            
        