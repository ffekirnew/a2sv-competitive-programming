def solve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                graph[i].append(j + 1)
    
    for node in range(n):
        print(len(graph[node]), *graph[node])


if __name__ == "__main__":
    solve()