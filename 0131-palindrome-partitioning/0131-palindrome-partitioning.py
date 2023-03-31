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
                if is_palindrome(temp):
                    curr_strings.append(temp)
                    backtrack(curr_strings, i + 1)
                    curr_strings.pop()

        
        def is_palindrome(string: str) -> bool:
            i, j = 0, len(string) - 1
            
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        # collect answers
        answer = []
        
        # do something
        
        backtrack([], 0)
        
        # return the answer
        return answer
                
        