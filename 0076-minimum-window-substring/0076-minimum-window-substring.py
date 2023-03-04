class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_ = len(s) + 1
        answer = [-1, -1]
        
        t_freq = Counter(t)
        t = set(t)
        seen = defaultdict(int)
        
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] in t_freq:
                    t_freq[ s[r] ] -= 1

                    if not t_freq[ s[r] ]:
                        del t_freq[ s[r] ]
            elif s[r] in t:
                seen[ s[r] ] += 1

            while l < len(s) and not t_freq:
                if min_ > r - l + 1:
                    min_ = min( min_, r - l + 1 )
                    answer[0] = l
                    answer[1] = r
                if s[l] in t:
                    if s[l] in seen:
                        seen[ s[l] ] -= 1
                        if not seen[ s[l] ]:
                            del seen[ s[l] ]
                    else:
                        t_freq[ s[l] ] = 1
                l += 1
                
            r += 1            
        
        return s[ answer[0] : answer[1] + 1 ] if answer != [-1, -1] else ""
            
            
        