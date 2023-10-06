from math import inf


def solve():
    number_of_nodes, number_of_edges = list(map(int, input().split()))
    edges = []
    for _ in range(number_of_edges):
        edges.append(list(map(int, input().split())))

    DEFAULT_DISCONNECTED_VALUE = 30_000
    distances = [float("inf")] * number_of_nodes
    distances[0] = 0

    RELAXATIONS = number_of_nodes - 1
    for _ in range(RELAXATIONS):
        for from_, to_, weight in edges:
            if (
                distances[from_ - 1] != float("inf")
                and distances[from_ - 1] + weight < distances[to_ - 1]
            ):
                distances[to_ - 1] = distances[from_ - 1] + weight

    answer = [val if val != inf else DEFAULT_DISCONNECTED_VALUE for val in distances]
    print(*answer)


if __name__ == "__main__":
    solve()
