def solve():
    n = int(input())
    ops = int(input())

    graph = { _ : [] for _ in range(1, n + 1) }

    for _ in range(ops):
        op = list(map(int, input().split()))

        if len(op) == 2:
            print(*graph[op[1]])
        else:
            graph[op[1]].append(op[2])
            graph[op[2]].append(op[1])

if __name__ == "__main__":
    solve()