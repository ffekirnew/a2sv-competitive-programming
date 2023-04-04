class Solution:
    def partitionString(self, s: str) -> int:
        answer = 1
        curr_set = set()
        
        for char in s:
            if char in curr_set:
                curr_set.clear()
                answer += 1

            curr_set.add(char)
        
        return answer
            
        