class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # create the object to be returned
        answer = []

        # do the solution
        def backtrack(curr_combination=[], next_start=1):
            if k - len(curr_combination) == 0:
                answer.append(curr_combination[:])
                return
            
            for candidate in range(next_start, n + 1):
                curr_combination += [candidate]
                backtrack(curr_combination, candidate + 1)
                curr_combination.pop()

        backtrack()
        # return the solution
        return answer