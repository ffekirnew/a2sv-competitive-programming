def solve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    sources = set(range(n))
    sinks = set(range(n))

    for start in range(n):
        for dest in range(n):
            if grid[start][dest]:
                if dest in sources:
                    sources.remove(dest)
                if start in sinks:
                    sinks.remove(start)
    
    sources = list(map( lambda x: x + 1, list(sources) ))
    sinks = list(map( lambda x: x + 1, list(sinks) ))

    print(len(sources), *sources)
    print(len(sinks), *sinks)


if __name__ == "__main__":
    solve()