class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        t_freq = Counter(t)
        
        answer = 0
        
        for char in t_freq.keys():
            if (t_freq[char] - s_freq[char]) > 0:
                answer += (t_freq[char] - s_freq[char])
                
        return answer
        