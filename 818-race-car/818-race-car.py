class Solution:
    def racecar(self, target: int) -> int:
        def successor_states(p, s):
            return [(p + s, s * 2), (p, 1 if s <= 0 else -1)]

        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])

        while queue:
            position, speed, path_length = queue.popleft()
            
            if position == target:
                return path_length
            
            for new_position, new_speed in successor_states(position, speed):
                if (new_position, new_speed) not in visited:
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed, path_length + 1))
        
        return -1