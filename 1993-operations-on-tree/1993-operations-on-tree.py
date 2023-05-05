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
        while self.parent[num] != -1:
            if self.parent[num] in self.locked:
                return True
            
            num = self.parent[num]
        
        return False       
    
    def descendant_locked(self, num) -> bool:
        queue = deque(self.children[num])
        while queue:
            node = queue.popleft()
            
            if node in self.locked:
                return True
            
            for child in self.children[node]:
                queue.append(child)
        
        return False
    
    def unlock_descendants(self, num) -> None:
        queue = deque(self.children[num])
        while queue:
            node = queue.popleft()
            
            if node in self.locked:
                del self.locked[node]
            
            for child in self.children[node]:
                queue.append(child)

    def upgrade(self, num: int, user: int) -> bool:
        # Condition 1: The node is unlocked,
        if num in self.locked:
            return False
        
        # Condition 2: It has at least one locked descendant (by any user)
        if not self.descendant_locked(num):
            return False
        
        # Condition 3: It does not have any locked ancestors.
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