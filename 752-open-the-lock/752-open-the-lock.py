class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(tuple(map(int, list(deadend))) for deadend in deadends)
        lock = [0, 0, 0, 0]
        target = list(map(int, list(target)))
        
        def next_lock_comb(lock, scroll):
            for i in range(4):
                lock[i] = (lock[i] + scroll[i]) % 10
            
            return lock
        
        DIRS = [[0, 0, 0, 1],[0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0],[0, 0, 0, -1],[0, 0, -1, 0], [0, -1, 0, 0], [-1, 0, 0, 0],]
        
        fringe = []
        visited = set(tuple(lock))
        
        if tuple(lock) not in deadends:
            fringe = [[lock, []]]
        
        while fringe:
            next_level = []
            
            for comb, path in fringe:
                if comb == target:
                    return len(path)

                for scroll in DIRS:
                    next_combination = next_lock_comb(comb.copy(), scroll)
                    
                    if tuple(next_combination) not in deadends and tuple(next_combination) not in visited:
                        visited.add(tuple(next_combination))
                        fringe.append([next_combination, path + [next_combination]])

            fringe = next_level
        
        return -1
        