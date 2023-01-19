from collections import defaultdict


if __name__ == "__main__":
    rows, cols = map(int, input().split())

    grid = []
    for row in range(rows):
        grid.append(list(input()))
    
    cols_freq = []
    rows_freq = []

    for r in range(rows):
        rows_freq.append(defaultdict(int))
        for c in range(cols):
            rows_freq[-1][grid[r][c]] += 1

    for c in range(cols):
        cols_freq.append(defaultdict(int))
        for r in range(rows):
            cols_freq[-1][grid[r][c]] += 1
    
    answer = []
    for row in range(rows):
        for col in range(cols):
            repeated = False
            if rows_freq[row][grid[row][col]] > 1:
                repeated = True
            if cols_freq[col][grid[row][col]] > 1:
                repeated = True
            
            if not repeated:
                answer.append(grid[row][col])
    
    print("".join(answer))
