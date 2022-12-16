class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = []
        rows = len(matrix)
        columns = len(matrix[0])
        for j in range(columns):
            answer.append([])
            for i in range(rows):
                answer[-1].append(matrix[i][j])
        return answer