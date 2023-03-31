class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(curr_strings, index):
            if index == len(s):
                if all( is_palindrome(string) for string in curr_strings ):
                    answer.append(curr_strings.copy())
                return
            
            backtrack(curr_strings + [s[index]], index + 1)
            if index:
                curr_strings[-1] += s[index]
                backtrack(curr_strings, index + 1 )

        
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
                
        