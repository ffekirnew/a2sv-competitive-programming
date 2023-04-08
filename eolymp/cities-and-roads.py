from collections import defaultdict


def solve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    graph = defaultdict(set)

    for i in range(n):
        for j in range(n):
            if i is not j and grid[i][j]:
                graph[i].add(j)
    
    answer = 0
    for i in range(n):
        answer += len(graph[i])
    
    print(answer // 2)

if __name__ == "__main__":
    solve()
