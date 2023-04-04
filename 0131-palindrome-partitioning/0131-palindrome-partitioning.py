class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(curr_strings, index):
            if index == len(s):
                if all( is_palindrome(string) for string in curr_strings ):
                    answer.append(curr_strings)
                return
            
            backtrack(curr_strings + [s[index]], index + 1)
            if index:
                curr_strings[-1] += s[index]
                backtrack(curr_strings, index + 1 )

        
        def is_palindrome(string: str) -> bool:
            for i in range(len(string) // 2):
                if string[i] != string[len(string) - i - 1]:
                    return False
            return True
        
        # collect answers
        answer = []
        
        # do something
        
        backtrack([], 0)
        
        # return the answer
        return answer
                
        