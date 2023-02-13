class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(reverse = True, key = lambda x: x[k])
        
        return score
        