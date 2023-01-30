num_tests = int(input())
answers = []  

for i in range(num_tests):
    # accept inputs
    rows, cols = map(int, input().split())

    # build the grid
    grid = []
    for row in range(rows):
        grid.append(list(map(int, input().split())))

    # collect the sums of each diagonals
    diagonals = []
    anti_diagonals = []
    diagonal_index = {}
    anti_diagonal_index = {}

    for row in range(1 - cols, rows):

        # forward diagonals
        r, c = row, 0
        diagonals.append(0)
        while r < rows and c < cols:
            if 0 <= r < rows and c < cols:
                diagonals[-1] += grid[r][c]
                diagonal_index[tuple([r, c])] = len(diagonals) - 1
            r += 1
            c += 1
        
        # anti diagonals
        r, c = row, cols - 1
        anti_diagonals.append(0)
        while r < rows and 0 <= c:
            if 0<= r < rows and 0 <= c:
                anti_diagonals[-1] += grid[r][c]
                anti_diagonal_index[tuple([r, c])] = len(diagonals) - 1
            r += 1
            c -= 1

    # traverse and pick the maximum
    answers.append(0)
    for r in range(rows):
        for c in range(cols):
            curr = diagonals[diagonal_index[tuple([r, c])]] + anti_diagonals[anti_diagonal_index[tuple([r, c])]] - grid[r][c]
            answers[-1] = max(curr, answers[-1])


for ans in answers:
    print(ans)