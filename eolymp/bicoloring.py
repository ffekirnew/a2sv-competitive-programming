from collections import defaultdict, deque

def solve():
    num_nodes = int(input())
    answers = []

    while num_nodes:
        answer = None

        num_edges = int(input())
        edges = [list(map(int, input().split())) for _ in range(num_edges)]

        graph = defaultdict(set)

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        colors = defaultdict(int)

        queue = deque([(1, 0)])
        visited = set([1])

        while queue:
            node, color = queue.popleft()

            if node in colors and colors[node] != color:
                answer = "NOT BICOLOURABLE."
                break

            colors[node] = color

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, 1 - color))

        if not answer and all(colors[from_] != colors[to_] for from_, to_ in edges):
            answer = "BICOLOURABLE."
        else:
            answer = "NOT BICOLOURABLE."
        
        answers.append(answer)
        num_nodes = int(input())
    
    for ans in answers:
        print(ans)
        

if __name__ == "__main__":
    solve()