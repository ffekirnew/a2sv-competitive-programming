class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        distance = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        bombs = [tuple(bomb + [i]) for i, bomb in enumerate(bombs)]
        
#         can_detonate = defaultdict(list)
#         for bomb in bombs:
#             for other_bomb in bombs:
#                 if bomb is not other_bomb and distance(bomb, other_bomb) <= bomb[2] ** 2:
#                     can_detonate[bomb].append(other_bomb)
        
#         print(can_detonate)
        
#         return 10

        def dfs(bomb, index):
            answer = 1
            
            for i in range(len(bombs)):
                if distance(bomb, bombs[i]) <= bomb[2] ** 2 and bombs[i] not in visited:
                    visited.add(bombs[i])
                    answer += dfs(bombs[i], i)
            
            return answer

        answer = 0
        for i in range(len(bombs)):
            visited = set([bombs[i]])
            answer = max(answer, dfs(bombs[i], i))
            
            if answer == len(bombs):
                break
        
        return answer
        