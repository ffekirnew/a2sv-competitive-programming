from collections import defaultdict


if __name__ == "__main__":
    # accept the input
    rows, cols = map(int, input().split())
    grid = []
    for row in range(rows):
        grid.append(list(input()))
    
    # count all columns and rows
    cols_freq = [defaultdict(int) for r in range(rows)]
    rows_freq = [defaultdict(int) for c in range(cols)]
    for r in range(rows):
        for c in range(cols):
            rows_freq[r][grid[r][c]] += 1
            cols_freq[c][grid[r][c]] += 1
    
    # construct the answer
    answer = []
    for row in range(rows):
        for col in range(cols):
            if not rows_freq[row][grid[row][col]] > 1 and not cols_freq[col][grid[row][col]] > 1:
                answer.append(grid[row][col])
    
    print("".join(answer))
