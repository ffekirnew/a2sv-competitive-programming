class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        curr_strings, index
        
        ["a", "aba", "aab"] 
        
        "b" s[index]
        
        """
        
        def backtrack(curr_strings, index):
            if index == len(s):
                answer.append(curr_strings.copy())
                return
            
            for i in range(index, len(s)):
                temp = s[index:i + 1]
                """
                index = 1
                [a] a
                """
                if s[index:i+1] == s[index:i+1][::-1]:
                    curr_strings.append(temp)
                    backtrack(curr_strings, i + 1)
                    curr_strings.pop()
        
        # collect answers
        answer = []
        
        # do something
        
        backtrack([], 0)
        
        # return the answer
        return answer
                
        