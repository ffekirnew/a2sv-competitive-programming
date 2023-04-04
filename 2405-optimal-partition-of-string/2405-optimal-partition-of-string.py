class Solution:
    def partitionString(self, s: str) -> int:
        answer = [[]]
        curr_set = set()
        
        for char in s:
            if char in curr_set:
                curr_set.clear()
                answer.append([])

            curr_set.add(char)
            answer[-1].append(s)
        
        return len(answer)
            
        