class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_mapping = {}
        t_to_s_mapping = {}
        for i in range(len(s)):
            if s[i] in s_to_t_mapping or t[i] in t_to_s_mapping:
                if s[i] in s_to_t_mapping and s_to_t_mapping[s[i]] != t[i]:
                    return False

                if t[i] in t_to_s_mapping and t_to_s_mapping[t[i]] != s[i]:
                    return False
            
            else:
                s_to_t_mapping[s[i]] = t[i]
                t_to_s_mapping[t[i]] = s[i]

        return True
        