class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # stores rows and cols for simpliciity
        rows = len(mat)
        cols = len(mat[0])
        
        # sanity check
        if rows * cols != r * c:
            return mat
        
        # create the object to be returned
        reshaped = []
        
        # do something
        loc = 0
        for i in range(r):
            reshaped.append([])
            for j in range(c):
                reshaped[-1].append(mat[loc // cols][loc % cols])
                loc += 1
                if loc == rows * cols:
                    break
                
        
        # return the solution
        return reshaped
        
        