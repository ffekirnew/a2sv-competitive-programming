class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = defaultdict(set)
        
        for i, node in enumerate(parent):
            self.children[node].add(i)
        
        self.locked = {}
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        self.locked[num] = user  
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            return False
        
        if user != self.locked[num]:
            return False
        
        del self.locked[num]
        return True
    
    def ancestor_locked(self, num) -> None:
        at_least_one_locked = False
        parent = self.parent[num]
        
        while parent != -1:
            at_least_one_locked |= parent in self.locked
            
            parent = self.parent[parent]
        
        return at_least_one_locked            
    
    def descendant_locked(self, num) -> bool:
        at_least_one_locked = False
        
        queue = deque(self.children[num])
        while queue:
            node = queue.popleft()
            
            at_least_one_locked |= node in self.locked
            
            for child in self.children[node]:
                queue.append(child)
        
        return at_least_one_locked
    
    def unlock_descendants(self, num) -> None:
        queue = deque(self.children[num])
        while queue:
            node = queue.popleft()
            
            if node in self.locked:
                del self.locked[node]
            
            for child in self.children[node]:
                queue.append(child)

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        if not self.descendant_locked(num):
            return False
        
        if self.ancestor_locked(num):
            return False
        
        self.unlock_descendants(num)
        self.locked[num] = user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)