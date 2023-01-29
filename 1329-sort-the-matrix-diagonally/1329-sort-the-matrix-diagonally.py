class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        # collect diagonals
        diagonals = []
        for start in range(1 - cols, rows):
            diagonals.append([])
            
            r, c = start, 0
            while r < rows and c < cols:
                if 0 <= r < rows and 0 <= c < cols:
                    diagonals[-1].append(mat[r][c])
                r += 1
                c += 1
                
        # sort all diagonals
        for i, diagonal in enumerate(diagonals):
            diagonals[i] = sorted(diagonal)
            
        # put the diagonals back in their place
        for start in range(1 - cols, rows):
            diagonal = diagonals[start + cols - 1]
            
            r, c, diagonal_idx = start, 0, 0
            while r < rows and c < cols and diagonal_idx < len(diagonal):
                if 0 <= r < rows and 0 <= c < cols:
                    mat[r][c] = diagonal[diagonal_idx]
                    diagonal_idx += 1
                r += 1
                c += 1
        
        return mat
        